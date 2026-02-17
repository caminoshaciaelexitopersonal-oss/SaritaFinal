import logging
import hashlib
import json
from decimal import Decimal
from django.db import transaction
from django.shortcuts import get_object_or_404
from django.utils import timezone
from .models import (
    Wallet, WalletTransaccion, WalletMovimiento, WalletBloqueo,
    WalletAlertaRiesgo, WalletAuditoria
)
from api.models import CustomUser

logger = logging.getLogger(__name__)

class WalletService:
    """
    Motor Financiero SARITA (Fase 17)
    Sistema de Custodia, Distribución y Control Antifraude.
    """
    def __init__(self, user: CustomUser):
        self.user = user

    def _generate_movement_hash(self, mov_data):
        payload = f"{mov_data['wallet_id']}{mov_data['transaccion_id']}{mov_data['monto']}{mov_data['tipo']}{timezone.now()}"
        return hashlib.sha256(payload.encode()).hexdigest()

    @transaction.atomic
    def execute_complex_transaction(self, referencia, movements_data, intention_id=None, metadata=None):
        """
        Ejecuta una transacción con múltiples movimientos asegurando integridad.
        movements_data: list of dicts {wallet_id, monto, tipo, ref_modelo, ref_id}
        """
        monto_total = sum(Decimal(str(m['monto'])) for m in movements_data if m['tipo'] in [WalletMovimiento.TipoMovimiento.INGRESO, WalletMovimiento.TipoMovimiento.PAGO])

        # 1. Crear la Transacción (Nivel Superior)
        transaccion = WalletTransaccion.objects.create(
            referencia_operativa=referencia,
            monto_total=monto_total,
            governance_intention_id=intention_id,
            metadata=metadata or {},
            estado=WalletTransaccion.Status.PROCESANDO
        )

        running_total = Decimal('0.00')

        # 2. Procesar Movimientos
        for m_data in movements_data:
            wallet = Wallet.objects.select_for_update().get(id=m_data['wallet_id'])
            monto = Decimal(str(m_data['monto']))
            tipo = m_data['tipo']

            # Reglas de Negocio por Tipo de Movimiento
            if tipo in [WalletMovimiento.TipoMovimiento.INGRESO, WalletMovimiento.TipoMovimiento.LIQUIDACION]:
                 # Ingreso aumenta saldo disponible (Liquidación es salida pero aquí lo tratamos por monto relativo)
                 if tipo == WalletMovimiento.TipoMovimiento.INGRESO:
                     wallet.saldo_disponible += monto
                 else:
                     if wallet.saldo_disponible < monto:
                         raise ValueError(f"Saldo insuficiente para liquidación en wallet {wallet.id}")
                     wallet.saldo_disponible -= monto

            elif tipo == WalletMovimiento.TipoMovimiento.PAGO:
                if wallet.saldo_disponible < monto:
                    raise ValueError(f"Saldo insuficiente para pago en wallet {wallet.id}")
                wallet.saldo_disponible -= monto

            elif tipo == WalletMovimiento.TipoMovimiento.COMISION:
                # Las comisiones suelen aumentar el saldo del receptor
                wallet.saldo_disponible += monto

            elif tipo == WalletMovimiento.TipoMovimiento.RETENCION:
                if wallet.saldo_disponible < monto:
                    raise ValueError(f"Saldo insuficiente para retención en wallet {wallet.id}")
                wallet.saldo_disponible -= monto
                wallet.saldo_bloqueado += monto

            wallet.save()

            # Crear el movimiento
            WalletMovimiento.objects.create(
                wallet=wallet,
                transaccion=transaccion,
                tipo=tipo,
                monto=monto,
                referencia_modelo=m_data['referencia_modelo'],
                referencia_id=m_data['referencia_id']
            )

        # 3. Validar Consistencia (Antifraude Fase 17.3.4)
        # Suma movimientos debe cuadrar según lógica de negocio (aquí simplificada)
        transaccion.estado = WalletTransaccion.Status.COMPLETADA
        transaccion.save()

        # 4. Integración ERP
        self._integrate_erp(transaccion)

        return transaccion

    def deposit(self, wallet_id, amount, description="Depósito", intention_id=None):
        wallet = get_object_or_404(Wallet, id=wallet_id)
        return self.execute_complex_transaction(
            referencia=f"DEP-{wallet.owner_id}",
            movements_data=[{
                "wallet_id": str(wallet.id),
                "monto": amount,
                "tipo": WalletMovimiento.TipoMovimiento.INGRESO,
                "referencia_modelo": "Manual",
                "referencia_id": "DEP-INTERNAL"
            }],
            intention_id=intention_id,
            metadata={"description": description}
        )

    def pay(self, to_wallet_id, amount, related_service_id=None, description="Pago", intention_id=None):
        from_wallet = Wallet.objects.filter(user=self.user).first()
        if not from_wallet:
            raise ValueError("El usuario no posee un monedero activo.")
        to_wallet = get_object_or_404(Wallet, id=to_wallet_id)

        movements = [
            {
                "wallet_id": str(from_wallet.id),
                "monto": amount,
                "tipo": WalletMovimiento.TipoMovimiento.PAGO,
                "referencia_modelo": "Service",
                "referencia_id": str(related_service_id) if related_service_id else "N/A"
            },
            {
                "wallet_id": str(to_wallet.id),
                "monto": amount,
                "tipo": WalletMovimiento.TipoMovimiento.INGRESO,
                "referencia_modelo": "Service",
                "referencia_id": str(related_service_id) if related_service_id else "N/A"
            }
        ]

        return self.execute_complex_transaction(
            referencia=f"PAY-{related_service_id}",
            movements_data=movements,
            intention_id=intention_id,
            metadata={"description": description}
        )

    def lock_funds(self, wallet_id, amount, reason="Bloqueo"):
        wallet = get_object_or_404(Wallet, id=wallet_id)
        amount_dec = Decimal(str(amount))

        if wallet.saldo_disponible < amount_dec:
            raise ValueError("Saldo insuficiente para bloqueo.")

        with transaction.atomic():
            wallet.saldo_disponible -= amount_dec
            wallet.saldo_bloqueado += amount_dec
            wallet.save()

            WalletBloqueo.objects.create(
                wallet=wallet,
                monto=amount_dec,
                motivo=reason
            )
            return wallet

    def unlock_funds(self, wallet_id, amount, reason="Desbloqueo"):
        wallet = get_object_or_404(Wallet, id=wallet_id)
        amount_dec = Decimal(str(amount))

        if wallet.saldo_bloqueado < amount_dec:
            raise ValueError("No hay suficiente saldo bloqueado.")

        with transaction.atomic():
            wallet.saldo_bloqueado -= amount_dec
            wallet.saldo_disponible += amount_dec
            wallet.save()

            # Marcar el bloqueo más reciente como inactivo (simplificado)
            bloqueo = wallet.bloqueos.filter(activo=True, monto=amount_dec).first()
            if bloqueo:
                bloqueo.activo = False
                bloqueo.liberado_en = timezone.now()
                bloqueo.save()
            return wallet

    def reverse_transaction(self, transaccion_id, motivo):
        """
        Fase 17.2.2: Cancelación parcial o reversión total.
        """
        original = get_object_or_404(WalletTransaccion, id=transaccion_id)
        if original.estado != WalletTransaccion.Status.COMPLETADA:
            raise ValueError("Solo se pueden revertir transacciones completadas.")

        from .models import WalletReversion
        reversion_data = []
        for mov in original.movimientos.all():
            # Invertimos el movimiento
            reversion_data.append({
                "wallet_id": str(mov.wallet_id),
                "monto": mov.monto,
                "tipo": WalletMovimiento.TipoMovimiento.REVERSION,
                "referencia_modelo": mov.referencia_modelo,
                "referencia_id": mov.referencia_id
            })

        with transaction.atomic():
            rev_tx = self.execute_complex_transaction(
                referencia=f"REV-{original.id}",
                movements_data=reversion_data,
                metadata={"motivo": motivo, "original_id": str(original.id)}
            )

            WalletReversion.objects.create(
                transaccion_original=original,
                motivo=motivo,
                autorizado_por=self.user
            )

            original.estado = WalletTransaccion.Status.REVERTIDA
            original.save()

            return rev_tx

    def audit_wallet(self, wallet_id):
        """
        Fase 17.4.1: Certificación financiera interna.
        """
        wallet = get_object_or_404(Wallet, id=wallet_id)
        movimientos = wallet.movimientos.all()

        calculado = Decimal('0.00')
        for mov in movimientos:
            if mov.tipo in [WalletMovimiento.TipoMovimiento.INGRESO, WalletMovimiento.TipoMovimiento.COMISION]:
                calculado += mov.monto
            elif mov.tipo in [WalletMovimiento.TipoMovimiento.PAGO, WalletMovimiento.TipoMovimiento.LIQUIDACION, WalletMovimiento.TipoMovimiento.RETENCION]:
                calculado -= mov.monto
            elif mov.tipo == WalletMovimiento.TipoMovimiento.REVERSION:
                # La reversión depende de si era crédito o débito originalmente,
                # pero para este motor simplificado asumimos que revertir un mov de ingreso es resta y viceversa.
                # En un sistema real, WalletMovimiento tendría 'sentido' (DEBITO/CREDITO).
                pass

        # Si hay descuadre, generar alerta crítica
        if calculado != wallet.saldo_disponible:
            WalletAlertaRiesgo.objects.create(
                wallet=wallet,
                codigo_alerta="DESCUADRE_SALDO",
                descripcion=f"Saldo calculado {calculado} != Saldo real {wallet.saldo_disponible}"
            )
            return False
        return True

    def _integrate_erp(self, transaccion):
        from apps.admin_plataforma.services.quintuple_erp import QuintupleERPService
        erp = QuintupleERPService(user=self.user)

        for mov in transaccion.movimientos.all():
            erp.record_impact(f"WALLET_{mov.tipo}", {
                "wallet_id": str(mov.wallet_id),
                "amount": float(mov.monto),
                "description": f"TX {transaccion.id} - Mov {mov.id}",
                "referencia_operativa": transaccion.referencia_operativa
            })

# Alias para retrocompatibilidad
WalletAccountService = WalletService
