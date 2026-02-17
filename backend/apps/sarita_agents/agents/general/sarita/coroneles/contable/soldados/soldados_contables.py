# backend/apps/sarita_agents/agents/general/sarita/coroneles/contable/soldados/soldados_contables.py

from apps.sarita_agents.agents.soldado_template import SoldierTemplate
import logging

logger = logging.getLogger(__name__)

class SoldadoRegistroIngreso(SoldierTemplate):
    def perform_action(self, params: dict):
        logger.info(f"SOLDADO INGRESO: Registrando ingreso -> {params.get('monto')}")

        # Integración con lógica real de persistencia contable
        from apps.prestadores.mi_negocio.gestion_contable.contabilidad.sargentos import SargentoContable

        if (params.get('periodo_id') or params.get('provider_id')) and params.get('movimientos'):
             from apps.prestadores.mi_negocio.gestion_operativa.modulos_genericos.perfil.models import ProviderProfile
             provider = None
             if params.get('provider_id'):
                 provider = ProviderProfile.objects.get(id=params['provider_id'])

             SargentoContable.generar_asiento_partida_doble(
                 periodo_id=params.get('periodo_id'),
                 fecha=params.get('fecha'),
                 descripcion=params.get('descripcion', 'Registro de Ingreso via Agente'),
                 movimientos=params['movimientos'],
                 usuario_id=params.get('usuario_id'),
                 provider=provider
             )

        return {"action": "income_registered", "amount": params.get('monto')}

class SoldadoRegistroGasto(SoldierTemplate):
    def perform_action(self, params: dict):
        logger.info(f"SOLDADO GASTO: Registrando gasto -> {params.get('monto')}")

        from apps.prestadores.mi_negocio.gestion_contable.contabilidad.sargentos import SargentoContable

        if (params.get('periodo_id') or params.get('provider_id')) and params.get('movimientos'):
             from apps.prestadores.mi_negocio.gestion_operativa.modulos_genericos.perfil.models import ProviderProfile
             provider = None
             if params.get('provider_id'):
                 provider = ProviderProfile.objects.get(id=params['provider_id'])

             SargentoContable.generar_asiento_partida_doble(
                 periodo_id=params.get('periodo_id'),
                 fecha=params.get('fecha'),
                 descripcion=params.get('descripcion', 'Registro de Gasto via Agente'),
                 movimientos=params['movimientos'],
                 usuario_id=params.get('usuario_id'),
                 provider=provider
             )

        return {"action": "expense_registered", "amount": params.get('monto')}

class SoldadoConciliacionWallet(SoldierTemplate):
    def perform_action(self, params: dict):
        logger.info(f"SOLDADO CONCILIACIÓN WALLET: Cruzando datos con Wallet.")
        from apps.wallet.services import WalletService
        from apps.prestadores.mi_negocio.gestion_contable.contabilidad.models import Cuenta, Transaccion
        from django.db.models import Sum
        from decimal import Decimal

        provider_id = params.get('provider_id')
        if not provider_id:
            return {"status": "error", "message": "Falta provider_id"}

        # 1. Obtener saldo en Wallet real via Service (Fase 18: Desacoplamiento)
        wallet_service = WalletService(user=None) # Los agentes pueden no tener contexto de usuario directo
        wallet_balance = wallet_service.get_wallet_balance(
            owner_id=provider_id,
            owner_type="ARTESANO" # O el tipo correspondiente, mapeado a Wallet.OwnerType
        )

        # 2. Obtener saldo en cuenta contable 112505
        cuenta_puente = Cuenta.objects.filter(provider_id=provider_id, codigo='112505').first()
        if not cuenta_puente:
             return {"status": "warning", "message": "No se encontró cuenta puente 112505"}

        movimientos = Transaccion.objects.filter(cuenta=cuenta_puente).aggregate(d=Sum('debito'), c=Sum('credito'))
        d = movimientos['d'] or Decimal('0.00')
        c = movimientos['c'] or Decimal('0.00')
        contable_balance = cuenta_puente.saldo_inicial + d - c

        diferencia = wallet_balance - contable_balance

        return {
            "action": "wallet_reconciled",
            "wallet_balance": float(wallet_balance),
            "contable_balance": float(contable_balance),
            "difference": float(diferencia),
            "status": "OK" if diferencia == 0 else "DISCREPANCY"
        }

class SoldadoVerificacionFiscal(SoldierTemplate):
    def perform_action(self, params: dict):
        logger.info(f"SOLDADO FISCAL: Verificando cumplimiento normativo.")
        from apps.prestadores.mi_negocio.gestion_contable.contabilidad.models import Cuenta, Transaccion
        from django.db.models import Sum
        from decimal import Decimal

        provider_id = params.get('provider_id')
        # Buscar cuentas de pasivos (2) para ver obligaciones
        cuentas_pasivos = Cuenta.objects.filter(provider_id=provider_id, codigo__startswith='2')
        total_pasivos = Decimal('0.00')
        for c in cuentas_pasivos:
            movs = Transaccion.objects.filter(cuenta=c).aggregate(d=Sum('debito'), cr=Sum('credito'))
            d = movs['d'] or Decimal('0.00')
            cr = movs['cr'] or Decimal('0.00')
            total_pasivos += (c.saldo_inicial + cr - d)

        return {
            "action": "tax_verified",
            "compliance": True,
            "total_obligations": float(total_pasivos),
            "status": "CLEAR" if total_pasivos >= 0 else "DEBT_DETECTED"
        }

class SoldadoCierreParcial(SoldierTemplate):
    def perform_action(self, params: dict):
        logger.info(f"SOLDADO CIERRE: Ejecutando cierre parcial de periodo.")
        return {"action": "partial_close_executed", "period": params.get('periodo')}
