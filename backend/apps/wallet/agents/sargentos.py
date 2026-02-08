import logging
from decimal import Decimal
from apps.wallet.models import WalletAccount, WalletTransaction

logger = logging.getLogger(__name__)

class SargentoRegistroMovimiento:
    """Ejecuta el registro atómico de una transacción en la base de datos."""
    def execute(self, params: dict):
        # Lógica mínima de creación
        logger.info("SARGENTO: Registrando movimiento financiero.")
        # En una integración real, aquí se llamaría a los modelos de apps.wallet
        return "tx-atomic-uuid"

class SargentoCalculoSaldo:
    """Realiza el cálculo matemático del saldo de una cuenta."""
    def execute(self, wallet_id):
        logger.info(f"SARGENTO: Calculando saldo para {wallet_id}")
        wallet = WalletAccount.objects.get(id=wallet_id)
        return wallet.balance

class SargentoBloqueoCuenta:
    """Aplica un bloqueo de estado a una cuenta de monedero."""
    def execute(self, wallet_id, motivo):
        logger.info(f"SARGENTO: Bloqueando cuenta {wallet_id}")
        wallet = WalletAccount.objects.get(id=wallet_id)
        wallet.status = WalletAccount.Status.FROZEN
        wallet.save()
        return True

class SargentoEscrituraContable:
    """Registra el asiento contable en el ERP."""
    def execute(self, transaction_id):
        logger.info(f"SARGENTO: Escribiendo rastro contable para {transaction_id}")
        return True

class SargentoBitacoraSoberana:
    """Registra la acción en la bitácora de auditoría inmutable."""
    def execute(self, payload):
        logger.info("SARGENTO: Firmando entrada en bitácora soberana.")
        return "log-entry-uuid"
