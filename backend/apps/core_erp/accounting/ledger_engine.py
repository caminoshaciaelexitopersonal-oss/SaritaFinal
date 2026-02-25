import logging
import hashlib
import json
from decimal import Decimal
from django.db import transaction
from django.utils import timezone
from .models import JournalEntry, LedgerEntry, Account, FiscalPeriod
from .exceptions import (
    UnbalancedEntryError, InactiveAccountError,
    FiscalPeriodClosedError, TenantMismatchError, DuplicateReversalError
)
from .posting_rules import PostingRules
from .journal_service import JournalService

logger = logging.getLogger(__name__)

class LedgerEngine:
    """
    Motor Contable Soberano del Core ERP.
    Único componente autorizado para crear asientos, validar doble partida e impactar balances.
    """

    @staticmethod
    def calculate_hash(entry: JournalEntry):
        """
        Calcula un hash SHA-256 de los datos del asiento para garantizar integridad.
        """
        data = {
            "id": str(entry.id),
            "tenant_id": str(entry.tenant_id),
            "date": str(entry.date),
            "lines": [
                {
                    "account": line.account.code,
                    "debit": str(line.debit_amount),
                    "credit": str(line.credit_amount),
                    "currency": line.currency
                }
                for line in entry.lines.all().order_by('id')
            ]
        }
        encoded = json.dumps(data, sort_keys=True).encode()
        return hashlib.sha256(encoded).hexdigest()

    @staticmethod
    def validate_balance(entry: JournalEntry):
        """
        Garantiza el principio de partida doble (Débitos = Créditos).
        """
        lines = entry.lines.all()
        if not lines:
            raise UnbalancedEntryError("Journal entry has no lines.")

        total_debit = sum(line.debit_amount for line in lines)
        total_credit = sum(line.credit_amount for line in lines)

        if abs(total_debit - total_credit) > Decimal('0.001'):
            raise UnbalancedEntryError(
                f"Asiento descuadrado {entry.id}. Débito: {total_debit}, Crédito: {total_credit}."
            )
        return True

    @staticmethod
    @transaction.atomic
    def post_event(event_type: str, payload: dict):
        """
        Método Central: Procesa un evento de negocio y genera el impacto contable real.
        Garantiza idempotencia y atomicidad estricta.
        Incluye monitoreo de performance (Fase 6.6).
        """
        import time
        start_time = time.time()
        logger.info(f"LedgerEngine: Procesando evento {event_type}")

        tenant_id = payload.get("tenant_id") or payload.get("organization_id")
        if not tenant_id:
             raise ValueError("tenant_id es obligatorio en el payload del evento contable.")

        # 1. Verificación de Idempotencia (Fase 6.1.2)
        financial_event_id = payload.get("financial_event_id") or payload.get("reference")
        if financial_event_id:
            existing = JournalEntry.objects.filter(
                tenant_id=tenant_id,
                financial_event_id=financial_event_id
            ).first()
            if existing:
                logger.warning(f"Evento {financial_event_id} ya procesado. Omitiendo duplicado.")
                return existing

        # 2. Obtener regla desde posting_rules
        lines_data = PostingRules.get_rule_for_event(event_type, payload)
        if not lines_data:
            logger.info(f"No hay reglas contables definidas para el evento {event_type}. Saltando.")
            return None

        # 3. Generar JournalEntry y Líneas LedgerEntry vía JournalService
        from ..observability.middleware import get_correlation_id

        entry = JournalService.create_entry(
            tenant_id=str(tenant_id),
            entry_date=timezone.now().date(),
            description=f"Impacto automático: {event_type}",
            lines_data=lines_data,
            reference=str(payload.get("reference", ""))
        )

        entry.event_type = event_type
        entry.financial_event_id = financial_event_id
        entry.correlation_id = payload.get('_correlation_id') or get_correlation_id()
        entry.rule_version = PostingRules.VERSION
        entry.save()

        # 4. Validar y Postear definitivamente
        result = LedgerEngine.post_entry(entry.id)

        duration = time.time() - start_time
        logger.info(f"LedgerEngine: Evento {event_type} procesado en {duration:.4f}s")
        return result

    @staticmethod
    @transaction.atomic
    def post_entry(entry_id: str):
        """
        Realiza la contabilización definitiva de un asiento.
        Implementa protección contra race conditions bloqueando filas críticas.
        """
        entry = JournalEntry.objects.select_for_update().get(id=entry_id)
        if entry.is_posted:
            return entry

        if entry.period.status != 'open':
            raise FiscalPeriodClosedError(f"Periodo fiscal {entry.period.id} está cerrado.")

        # 1. Bloqueo de Cuentas para consistencia (Fase 6.1.3)
        account_ids = entry.lines.values_list('account_id', flat=True)
        # Forzar select_for_update en cuentas involucradas
        list(Account.plain_objects.select_for_update().filter(id__in=account_ids))

        # 2. Validaciones de Integridad
        LedgerEngine.validate_balance(entry)

        # Verificar que todas las cuentas estén activas
        for line in entry.lines.all():
            if not line.account.is_active:
                raise InactiveAccountError(f"La cuenta {line.account.code} está inactiva.")
            if str(line.account.tenant_id) != str(entry.tenant_id):
                raise TenantMismatchError(f"Cuenta {line.account.code} no pertenece al tenant {entry.tenant_id}")

        # 3. Multi-Currency Logic (Phase B)
        # Standardize transaction vs base amounts
        exchange_rate = getattr(entry, 'exchange_rate', Decimal('1.0'))
        for line in entry.lines.all():
            # If not explicitly set, use debit/credit as transaction amount
            if not line.amount_transaction:
                line.amount_transaction = line.debit_amount if line.debit_amount > 0 else line.credit_amount

            line.amount_base = line.amount_transaction * exchange_rate
            line.save()

        # 4. Audit Integrity Hardening (Phase B)
        entry.system_hash = LedgerEngine.calculate_hash(entry)
        entry.immutable_signature = f"LEDGER-SIG-{entry.system_hash[:16]}-{timezone.now().timestamp()}"
        entry.posted_at = timezone.now()

        # 5. Posteo Final
        entry.is_posted = True
        entry.save()

        logger.info(f"JournalEntry {entry.id} posteado exitosamente con Hash: {entry.system_hash}")
        return entry

    @staticmethod
    @transaction.atomic
    def reverse_entry(journal_entry_id: str, reason: str = "Reversión automática"):
        """
        Genera un contra-asiento para anular una operación. Inmutabilidad total.
        """
        original = JournalEntry.objects.get(id=journal_entry_id)

        if original.is_reversal:
            raise DuplicateReversalError("No se puede reversar un asiento que ya es una reversión.")

        if JournalEntry.objects.filter(reversed_entry_id=journal_entry_id).exists():
            raise DuplicateReversalError("Este asiento ya ha sido reversado previamente.")

        # Crear nuevo JournalEntry de reversión
        reversal = JournalEntry.objects.create(
            tenant_id=original.tenant_id,
            period=original.period,
            date=timezone.now().date(),
            description=f"REVERSIÓN de {original.id}: {reason}",
            reference=original.reference,
            is_reversal=True,
            reversed_entry_id=original.id
        )

        # Invertir Débitos y Créditos de las líneas
        for line in original.lines.all():
            LedgerEntry.objects.create(
                journal_entry=reversal,
                account=line.account,
                debit_amount=line.credit_amount,
                credit_amount=line.debit_amount,
                description=f"Rev: {line.description}"
            )

        return LedgerEngine.post_entry(reversal.id)

    @staticmethod
    def get_trial_balance(tenant_id: str, cutoff_date=None):
        """
        Genera un balance de prueba consolidando saldos de cuentas.
        """
        if cutoff_date is None:
            cutoff_date = timezone.now().date()
        from .reports_engine import ReportsEngine
        return ReportsEngine.get_trial_balance(tenant_id, cutoff_date)
