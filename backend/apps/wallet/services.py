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

    def deposit(self, wallet_id, amount, description="Depósito de fondos", intention_id=None):
        # En este entorno, permitimos que el usuario deposite en su propia cuenta
        # o que el admin deposite en cualquier cuenta.
        wallet = get_object_or_404(WalletAccount, id=wallet_id)

        if not self.user.is_superuser and wallet.user != self.user:
            raise PermissionError("No tiene permisos para depositar en esta cuenta.")

        with transaction.atomic():
            wallet.balance += Decimal(str(amount))
            wallet.save()

            tx = WalletTransaction.objects.create(
                to_wallet=wallet,
                amount=Decimal(str(amount)),
                type=WalletTransaction.TransactionType.DEPOSIT,
                status=WalletTransaction.Status.EXECUTED,
                description=description,
                governance_intention_id=intention_id,
                metadata={
                    "executed_by": self.user.username,
                    "method": "INSTITUTIONAL_GATEWAY"
                }
            )

            self._integrate_erp(tx)

            return tx

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

    def pay(self, to_wallet_id, amount, related_service_id=None, description="Pago de servicio", intention_id=None):
        from_wallet = WalletAccount.objects.filter(user=self.user).first()
        if not from_wallet:
            raise ValueError("El usuario no posee un monedero activo.")
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
                governance_intention_id=intention_id,
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
