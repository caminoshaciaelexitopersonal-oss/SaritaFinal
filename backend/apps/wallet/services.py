import logging
import hashlib
import json
from decimal import Decimal
from django.db import transaction, IntegrityError
from django.shortcuts import get_object_or_404
from django.utils import timezone
from .models import WalletAccount, WalletTransaction
from api.models import CustomUser

logger = logging.getLogger(__name__)

class WalletService:
    def __init__(self, user: CustomUser):
        self.user = user

    def _generate_transaction_hash(self, tx_data, previous_hash):
        """Genera un hash SHA-256 encadenado para la transacción."""
        content = json.dumps(tx_data, sort_keys=True, default=str)
        payload = f"{content}|{previous_hash}"
        return hashlib.sha256(payload.encode()).hexdigest()

    def _execute_ledger_transaction(self, from_wallet, to_wallet, amount, tx_type,
                                 description="", intention_id=None, related_service_id=None,
                                 idempotency_key=None, metadata=None):
        """
        Motor Transaccional Atómico con Ledger Inmutable y Idempotencia.
        """
        if idempotency_key:
            existing_tx = WalletTransaction.objects.filter(idempotency_key=idempotency_key).first()
            if existing_tx:
                logger.info(f"WALLET: Retornando transacción idempotente existente {existing_tx.id}")
                return existing_tx

        amount_dec = Decimal(str(amount))
        if amount_dec < 0:
            raise ValueError("El monto no puede ser negativo.")

        with transaction.atomic():
            # 1. Bloquear filas para evitar condiciones de carrera (select_for_update)
            if from_wallet:
                from_wallet = WalletAccount.objects.select_for_update().get(id=from_wallet.id)
                if from_wallet.balance < amount_dec:
                    raise ValueError(f"Saldo insuficiente en monedero {from_wallet.id}")
                if from_wallet.status != WalletAccount.Status.ACTIVE:
                    raise PermissionError(f"Monedero de origen {from_wallet.id} no está activo.")

            if to_wallet:
                to_wallet = WalletAccount.objects.select_for_update().get(id=to_wallet.id)

            # 2. Obtener el hash anterior del ledger
            last_tx = WalletTransaction.objects.order_by('-timestamp', '-id').first()
            prev_hash = last_tx.integrity_hash if last_tx else "GENESIS_BLOCK"

            # 3. Actualizar saldos
            if from_wallet:
                from_wallet.balance -= amount_dec
                from_wallet.save()

            if to_wallet:
                to_wallet.balance += amount_dec
                to_wallet.save()

            # 4. Crear registro en Ledger
            now = timezone.now()
            tx = WalletTransaction(
                idempotency_key=idempotency_key,
                from_wallet=from_wallet,
                to_wallet=to_wallet,
                amount=amount_dec,
                type=tx_type,
                status=WalletTransaction.Status.EXECUTED,
                description=description,
                governance_intention_id=intention_id,
                related_service_id=related_service_id,
                previous_hash=prev_hash,
                metadata=metadata or {},
                timestamp=now
            )

            # 5. Generar Integridad (Hash Chaining)
            tx_data = {
                "from": str(from_wallet.id) if from_wallet else None,
                "to": str(to_wallet.id) if to_wallet else None,
                "amount": str(amount_dec),
                "type": tx_type,
                "timestamp": str(now)
            }
            tx.integrity_hash = self._generate_transaction_hash(tx_data, prev_hash)

            # 6. Firma Digital Interna (Simulada para Fase 10)
            tx.signature = hashlib.sha256(f"{tx.integrity_hash}|SARITA_INTERNAL_KEY".encode()).hexdigest()

            tx.save()

            # 7. Impacto ERP
            self._integrate_erp(tx)

            return tx

    def recharge(self, wallet_id, amount, description="Recarga de fondos", idempotency_key=None):
        """Recarga manual o depósito."""
        wallet = get_object_or_404(WalletAccount, id=wallet_id)
        if not self.user.is_superuser:
            raise PermissionError("Solo administradores pueden realizar recargas manuales.")

        return self._execute_ledger_transaction(
            from_wallet=None,
            to_wallet=wallet,
            amount=amount,
            tx_type=WalletTransaction.TransactionType.RECHARGE,
            description=description,
            idempotency_key=idempotency_key,
            metadata={"executed_by": self.user.username}
        )

    def deposit(self, wallet_id, amount, description="Depósito de fondos", intention_id=None):
        wallet = get_object_or_404(WalletAccount, id=wallet_id)
        return self._execute_ledger_transaction(
            from_wallet=None,
            to_wallet=wallet,
            amount=amount,
            tx_type=WalletTransaction.TransactionType.DEPOSIT,
            description=description,
            intention_id=intention_id,
            metadata={"method": "INSTITUTIONAL_GATEWAY"}
        )

    def lock_funds(self, wallet_id, amount, reason="Reserva de fondos"):
        wallet = get_object_or_404(WalletAccount, id=wallet_id)
        amount_dec = Decimal(str(amount))

        if wallet.balance < amount_dec:
            raise ValueError("Saldo insuficiente para bloquear.")

        with transaction.atomic():
            wallet.balance -= amount_dec
            wallet.locked_balance += amount_dec
            wallet.save()

            logger.info(f"WALLET: Bloqueados {amount_dec} en cuenta {wallet.id}. Motivo: {reason}")
            return wallet

    def unlock_funds(self, wallet_id, amount, reason="Liberación de fondos"):
        wallet = get_object_or_404(WalletAccount, id=wallet_id)
        amount_dec = Decimal(str(amount))

        if wallet.locked_balance < amount_dec:
            raise ValueError("No hay suficiente saldo bloqueado.")

        with transaction.atomic():
            wallet.locked_balance -= amount_dec
            wallet.balance += amount_dec
            wallet.save()

            logger.info(f"WALLET: Liberados {amount_dec} en cuenta {wallet.id}. Motivo: {reason}")
            return wallet

    def pay(self, to_wallet_id, amount, related_service_id=None, description="Pago de servicio", intention_id=None, idempotency_key=None):
        from_wallet = WalletAccount.objects.filter(user=self.user).first()
        if not from_wallet:
            raise ValueError("El usuario no posee un monedero activo.")
        to_wallet = get_object_or_404(WalletAccount, id=to_wallet_id)

        return self._execute_ledger_transaction(
            from_wallet=from_wallet,
            to_wallet=to_wallet,
            amount=amount,
            tx_type=WalletTransaction.TransactionType.PAYMENT,
            description=description,
            intention_id=intention_id,
            related_service_id=related_service_id,
            idempotency_key=idempotency_key,
            metadata={"payer": self.user.username}
        )

    def transfer(self, to_wallet_id, amount, description="Transferencia interna", idempotency_key=None):
        from_wallet = WalletAccount.objects.filter(user=self.user).first()
        if not from_wallet:
            raise ValueError("El usuario no posee un monedero activo.")
        to_wallet = get_object_or_404(WalletAccount, id=to_wallet_id)

        return self._execute_ledger_transaction(
            from_wallet=from_wallet,
            to_wallet=to_wallet,
            amount=amount,
            tx_type=WalletTransaction.TransactionType.TRANSFER,
            description=description,
            idempotency_key=idempotency_key,
            metadata={"sender": self.user.username}
        )

    def pay_commission(self, to_wallet_id, amount, related_service_id=None, description="Pago de comisión"):
        """Paga comisión desde el monedero corporativo al destino."""
        corp_wallet = WalletAccount.objects.filter(owner_type=WalletAccount.OwnerType.CORPORATE).first()
        if not corp_wallet:
            # Auto-crear si no existe para evitar bloqueos en esta fase
            corp_wallet = WalletAccount.objects.create(
                owner_type=WalletAccount.OwnerType.CORPORATE,
                owner_id="INTERNAL_CORP",
                user=self.user, # Asignado al admin que lo dispara
                company=WalletAccount.objects.first().company if WalletAccount.objects.exists() else None,
                balance=Decimal('1000000000.00')
            )

        to_wallet = get_object_or_404(WalletAccount, id=to_wallet_id)

        return self._execute_ledger_transaction(
            from_wallet=corp_wallet,
            to_wallet=to_wallet,
            amount=amount,
            tx_type=WalletTransaction.TransactionType.COMMISSION,
            description=description,
            related_service_id=related_service_id,
            metadata={"source": "CORPORATE_CORE"}
        )

    def cashback(self, amount, description="Cashback por compra", idempotency_key=None):
        """Otorga cashback desde el corporativo al monedero del usuario."""
        corp_wallet = WalletAccount.objects.filter(owner_type=WalletAccount.OwnerType.CORPORATE).first()
        to_wallet = WalletAccount.objects.filter(user=self.user).first()

        return self._execute_ledger_transaction(
            from_wallet=corp_wallet,
            to_wallet=to_wallet,
            amount=amount,
            tx_type=WalletTransaction.TransactionType.CASHBACK,
            description=description,
            idempotency_key=idempotency_key,
            metadata={"type": "PROMOTIONAL"}
        )

    def reverse_transaction(self, transaction_id, reason="Reversión autorizada"):
        """Revierte formalmente una transacción."""
        original_tx = get_object_or_404(WalletTransaction, id=transaction_id)
        if original_tx.status != WalletTransaction.Status.EXECUTED:
            raise ValueError("No se puede revertir una transacción no ejecutada.")

        return self._execute_ledger_transaction(
            from_wallet=original_tx.to_wallet,
            to_wallet=original_tx.from_wallet,
            amount=original_tx.amount,
            tx_type=WalletTransaction.TransactionType.REVERSAL,
            description=f"Reversión de TX {original_tx.id}. Motivo: {reason}",
            metadata={"original_tx": str(original_tx.id)}
        )

    def freeze_account(self, wallet_id, reason):
        """Congela un monedero."""
        wallet = get_object_or_404(WalletAccount, id=wallet_id)
        wallet.status = WalletAccount.Status.FROZEN
        wallet.save()

        # Registrar en Ledger
        self._execute_ledger_transaction(
            from_wallet=None,
            to_wallet=None,
            amount=0,
            tx_type=WalletTransaction.TransactionType.FREEZE,
            description=f"Congelamiento de cuenta {wallet.id}. Motivo: {reason}",
            metadata={"wallet_id": str(wallet.id)}
        )
        return wallet

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
        Integración con los módulos del ERP Quíntuple (FASE 9).
        """
        from apps.admin_plataforma.services.quintuple_erp import QuintupleERPService
        erp_service = QuintupleERPService(user=self.user)

        # Determinamos el contexto del impacto
        # Buscamos si hay un servicio de delivery relacionado para extraer más contexto
        related_delivery_id = None
        if transaction.related_service_id:
            related_delivery_id = transaction.related_service_id

        company = transaction.to_wallet.company if transaction.to_wallet else transaction.from_wallet.company
        perfil_id = None

        if transaction.to_wallet and transaction.to_wallet.owner_type == WalletAccount.OwnerType.PROVIDER:
            perfil_id = transaction.to_wallet.owner_id
        elif transaction.from_wallet and transaction.from_wallet.owner_type == WalletAccount.OwnerType.PROVIDER:
            perfil_id = transaction.from_wallet.owner_id

        payload = {
            "company_id": str(company.id) if company else None,
            "perfil_id": str(perfil_id) if perfil_id else None,
            "cliente_id": str(self.user.id),
            "amount": float(transaction.amount),
            "description": transaction.description,
            "wallet_transaction_id": str(transaction.id),
            "delivery_service_id": str(related_delivery_id) if related_delivery_id else None
        }

        erp_service.record_impact(f"WALLET_{transaction.type}", payload)
