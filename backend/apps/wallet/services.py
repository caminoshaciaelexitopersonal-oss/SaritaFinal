import logging
from decimal import Decimal
from django.db import transaction
from django.shortcuts import get_object_or_404
from .models import WalletAccount, WalletTransaction
from api.models import CustomUser

logger = logging.getLogger(__name__)

class WalletService:
    def __init__(self, user: CustomUser):
        self.user = user

    def deposit(self, wallet_id, amount, description="Depósito de fondos"):
        wallet = get_object_or_404(WalletAccount, id=wallet_id)

        with transaction.atomic():
            wallet.balance += Decimal(str(amount))
            wallet.save()

            tx = WalletTransaction.objects.create(
                to_wallet=wallet,
                amount=Decimal(str(amount)),
                type=WalletTransaction.TransactionType.DEPOSIT,
                status=WalletTransaction.Status.EXECUTED,
                description=description,
                metadata={"executed_by": self.user.username}
            )

            self._integrate_erp(tx)

            return tx

    def pay(self, to_wallet_id, amount, related_service_id=None, description="Pago de servicio"):
        from_wallet = WalletAccount.objects.get(user=self.user) # Assuming 1 wallet per user for now
        to_wallet = get_object_or_404(WalletAccount, id=to_wallet_id)
        amount_dec = Decimal(str(amount))

        if from_wallet.balance < amount_dec:
            raise ValueError("Saldo insuficiente en el monedero.")

        if from_wallet.status != WalletAccount.Status.ACTIVE:
            raise PermissionError("El monedero de origen no está activo.")

        with transaction.atomic():
            from_wallet.balance -= amount_dec
            from_wallet.save()

            to_wallet.balance += amount_dec
            to_wallet.save()

            tx = WalletTransaction.objects.create(
                from_wallet=from_wallet,
                to_wallet=to_wallet,
                amount=amount_dec,
                type=WalletTransaction.TransactionType.PAYMENT,
                status=WalletTransaction.Status.EXECUTED,
                related_service_id=related_service_id,
                description=description,
                metadata={"payer": self.user.username}
            )

            self._integrate_erp(tx)

            return tx

    def refund(self, transaction_id):
        original_tx = get_object_or_404(WalletTransaction, id=transaction_id)

        if original_tx.status != WalletTransaction.Status.EXECUTED:
            raise ValueError("Solo se pueden reembolsar transacciones ejecutadas.")

        if original_tx.type != WalletTransaction.TransactionType.PAYMENT:
            raise ValueError("Solo se pueden reembolsar pagos.")

        with transaction.atomic():
            # Revertir saldos
            from_wallet = original_tx.from_wallet
            to_wallet = original_tx.to_wallet
            amount = original_tx.amount

            to_wallet.balance -= amount
            to_wallet.save()

            from_wallet.balance += amount
            from_wallet.save()

            refund_tx = WalletTransaction.objects.create(
                from_wallet=to_wallet,
                to_wallet=from_wallet,
                amount=amount,
                type=WalletTransaction.TransactionType.REFUND,
                status=WalletTransaction.Status.EXECUTED,
                related_service_id=original_tx.related_service_id,
                description=f"Reembolso de transacción {original_tx.id}",
                metadata={"refunded_by": self.user.username, "original_tx": str(original_tx.id)}
            )

            original_tx.status = WalletTransaction.Status.REVERSED
            original_tx.save()

            self._integrate_erp(refund_tx)

            return refund_tx

    def liquidate(self, wallet_id):
        wallet = get_object_or_404(WalletAccount, id=wallet_id)
        amount = wallet.balance

        if amount <= 0:
            raise ValueError("No hay saldo para liquidar.")

        with transaction.atomic():
            wallet.balance = 0
            wallet.save()

            tx = WalletTransaction.objects.create(
                from_wallet=wallet,
                amount=amount,
                type=WalletTransaction.TransactionType.LIQUIDATION,
                status=WalletTransaction.Status.EXECUTED,
                description="Liquidación total de fondos",
                metadata={"liquidated_by": self.user.username}
            )

            self._integrate_erp(tx)

            return tx

    def freeze(self, wallet_id, motivo):
        wallet = get_object_or_404(WalletAccount, id=wallet_id)
        wallet.status = WalletAccount.Status.FROZEN
        wallet.save()

        logger.warning(f"WALLET: Cuenta {wallet.id} congelada por {self.user.username}. Motivo: {motivo}")
        return wallet

    def _integrate_erp(self, transaction: WalletTransaction):
        """
        Integración con los módulos del ERP Quíntuple.
        """
        logger.info(f"ERP INTEGRATION: Procesando transacción {transaction.id}")

        # 1. Gestión Contable: Asiento automático
        self._create_accounting_entry(transaction)

        # 2. Gestión Financiera: Flujo de caja / Orden de pago
        self._update_financial_state(transaction)

        # 3. Gestión Archivística: Evidencia legal
        self._generate_archival_evidence(transaction)

    def _create_accounting_entry(self, transaction: WalletTransaction):
        try:
            from apps.prestadores.mi_negocio.gestion_contable.contabilidad.models import AsientoContable, Transaccion, PeriodoContable, Cuenta
            # Esto es una simplificación, en un sistema real buscaríamos el periodo activo y las cuentas correctas del plan
            # Para esta implementación, buscaremos o crearemos lo mínimo necesario para que sea trazable.

            # Buscamos un periodo activo para la compañía
            periodo = PeriodoContable.objects.filter(provider_id=transaction.to_wallet.company_id if transaction.to_wallet else transaction.from_wallet.company_id, cerrado=False).first()
            if not periodo:
                logger.error("No hay periodo contable abierto para integración.")
                return

            asiento = AsientoContable.objects.create(
                provider_id=periodo.provider_id,
                periodo=periodo,
                fecha=transaction.timestamp.date(),
                descripcion=f"Movimiento Monedero SARITA - TX {transaction.id}",
                creado_por=self.user
            )

            # Registro simplificado de partida doble (Caja vs Monedero)
            # En producción esto depende del tipo de transacción
            # Supongamos una cuenta genérica para monedero

            # Debito / Crédito según tipo
            if transaction.type == WalletTransaction.TransactionType.PAYMENT:
                # El prestador recibe (to_wallet)
                # DEBITO a Monedero (Activo aumenta)
                # CREDITO a Ingresos por Servicios
                pass # Implementar lógica específica de cuentas si están configuradas

            logger.info(f"Asiento contable creado para TX {transaction.id}")
        except ImportError:
            logger.warning("Módulo contable no disponible para integración.")
        except Exception as e:
            logger.error(f"Error en integración contable: {e}")

    def _update_financial_state(self, transaction: WalletTransaction):
        try:
            import uuid as uuid_lib
            from apps.prestadores.mi_negocio.gestion_financiera.models import OrdenPago

            # Buscamos el perfil del prestador si aplica
            perfil_id = None
            if transaction.to_wallet and transaction.to_wallet.owner_type == WalletAccount.OwnerType.PROVIDER:
                perfil_id = transaction.to_wallet.owner_id
            elif transaction.from_wallet and transaction.from_wallet.owner_type == WalletAccount.OwnerType.PROVIDER:
                perfil_id = transaction.from_wallet.owner_id

            if transaction.type == WalletTransaction.TransactionType.LIQUIDATION and perfil_id:
                OrdenPago.objects.create(
                    perfil_ref_id=uuid_lib.UUID(perfil_id),
                    monto=transaction.amount,
                    fecha_pago=transaction.timestamp.date(),
                    concepto=f"Liquidación Monedero SARITA {transaction.id}",
                    estado=OrdenPago.EstadoPago.PENDIENTE
                )
            logger.info(f"Estado financiero actualizado para TX {transaction.id}")
        except Exception as e:
            logger.error(f"Error en integración financiera: {e}")

    def _generate_archival_evidence(self, transaction: WalletTransaction):
        try:
            from apps.prestadores.mi_negocio.gestion_archivistica.models import Document, DocumentType, Process, ProcessType

            company = transaction.to_wallet.company if transaction.to_wallet else transaction.from_wallet.company

            # Buscamos o creamos el tipo de documento para comprobantes financieros
            doc_type, _ = DocumentType.objects.get_or_create(
                company=company,
                code="COMP_FIN",
                defaults={"name": "Comprobante Financiero"}
            )

            # Buscamos o creamos el proceso de Tesorería
            proc_type, _ = ProcessType.objects.get_or_create(
                company=company,
                code="TES",
                defaults={"name": "Tesorería"}
            )

            process, _ = Process.objects.get_or_create(
                company=company,
                process_type=proc_type,
                code="TES-WAL",
                defaults={"name": "Gestión de Monedero"}
            )

            # Creamos el documento
            doc = Document.objects.create(
                company=company,
                process=process,
                document_type=doc_type,
                sequence=Document.objects.filter(company=company).count() + 1,
                document_code=f"WAL-{transaction.id.hex[:8]}",
                created_by=self.user
            )

            transaction.metadata["archival_document_id"] = str(doc.id)
            transaction.save()

            logger.info(f"Evidencia archivística generada: {doc.document_code}")
        except Exception as e:
            logger.error(f"Error en integración archivística: {e}")
