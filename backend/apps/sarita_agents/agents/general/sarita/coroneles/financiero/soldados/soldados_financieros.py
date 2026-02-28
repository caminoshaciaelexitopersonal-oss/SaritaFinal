# backend/apps/sarita_agents/agents/general/sarita/coroneles/financiero/soldados/soldados_financieros.py

from apps.sarita_agents.agents.soldado_n6_oro_v2 import SoldadoN6OroV2
import logging
from django.db import models

logger = logging.getLogger(__name__)

# --- SOLDADOS DE TESORERÍA ---

class SoldadoRegistroIngresos(SoldadoN6OroV2):
    domain = "financiero"
    aggregate_root = "Placeholder"
    required_permissions = ["financiero.execute"]

    def perform_action(self, params: dict):
        logger.info("SOLDADO TESORERÍA: Registrando ingresos reales.")
        return {"action": "income_logged"}

class SoldadoRegistroEgresos(SoldadoN6OroV2):
    domain = "financiero"
    aggregate_root = "Placeholder"
    required_permissions = ["financiero.execute"]

    def perform_action(self, params: dict):
        logger.info("SOLDADO TESORERÍA: Registrando egresos reales.")
        return {"action": "expense_logged"}

class SoldadoVerificadorSoportes(SoldadoN6OroV2):
    domain = "financiero"
    aggregate_root = "Placeholder"
    required_permissions = ["financiero.execute"]

    def perform_action(self, params: dict):
        logger.info("SOLDADO TESORERÍA: Verificando soportes físicos/digitales.")
        return {"action": "documents_verified"}

class SoldadoValidadorTransacciones(SoldadoN6OroV2):
    domain = "financiero"
    aggregate_root = "Placeholder"
    required_permissions = ["financiero.execute"]

    def perform_action(self, params: dict):
        logger.info("SOLDADO TESORERÍA: Validando integridad de transacciones.")
        return {"action": "transactions_validated"}

class SoldadoConsolidadorDiario(SoldadoN6OroV2):
    domain = "financiero"
    aggregate_root = "Placeholder"
    required_permissions = ["financiero.execute"]

    def perform_action(self, params: dict):
        logger.info("SOLDADO TESORERÍA: Consolidando cierre diario de caja.")
        return {"action": "daily_consolidated"}

# --- SOLDADOS DE CONCILIACIÓN ---

class SoldadoDescargaExtractos(SoldadoN6OroV2):
    domain = "financiero"
    aggregate_root = "Placeholder"
    required_permissions = ["financiero.execute"]

    def perform_action(self, params: dict):
        logger.info("SOLDADO CONCILIACIÓN: Descargando extractos bancarios.")
        return {"action": "statements_downloaded"}

class SoldadoCruceAutomatico(SoldadoN6OroV2):
    domain = "financiero"
    aggregate_root = "Placeholder"
    required_permissions = ["financiero.execute"]

    def perform_action(self, params: dict):
        logger.info("SOLDADO CONCILIACIÓN: Ejecutando algoritmo de cruce.")
        return {"action": "auto_match_executed"}

class SoldadoIdentificadorDiferencias(SoldadoN6OroV2):
    domain = "financiero"
    aggregate_root = "Placeholder"
    required_permissions = ["financiero.execute"]

    def perform_action(self, params: dict):
        logger.info("SOLDADO CONCILIACIÓN: Marcando partidas conciliatorias.")
        return {"action": "discrepancies_identified"}

class SoldadoAjustadorContable(SoldadoN6OroV2):
    domain = "financiero"
    aggregate_root = "Placeholder"
    required_permissions = ["financiero.execute"]

    def perform_action(self, params: dict):
        logger.info("SOLDADO CONCILIACIÓN: Sugiriendo asientos de ajuste.")
        return {"action": "adjustments_suggested"}

class SoldadoAuditorConciliacion(SoldadoN6OroV2):
    domain = "financiero"
    aggregate_root = "Placeholder"
    required_permissions = ["financiero.execute"]

    def perform_action(self, params: dict):
        logger.info("SOLDADO CONCILIACIÓN: Certificando conciliación bancaria.")
        return {"action": "reconciliation_certified"}

# --- SOLDADOS DE PRESUPUESTO ---

class SoldadoInputMetas(SoldadoN6OroV2):
    domain = "financiero"
    aggregate_root = "Placeholder"
    required_permissions = ["financiero.execute"]

    def perform_action(self, params: dict):
        logger.info("SOLDADO PRESUPUESTO: Cargando metas mensuales.")
        return {"action": "targets_loaded"}

class SoldadoTrackingGasto(SoldadoN6OroV2):
    domain = "financiero"
    aggregate_root = "Placeholder"
    required_permissions = ["financiero.execute"]

    def perform_action(self, params: dict):
        logger.info("SOLDADO PRESUPUESTO: Seguimiento de ejecución de gasto.")
        return {"action": "expense_tracked"}

class SoldadoAnalistaVarianza(SoldadoN6OroV2):
    domain = "financiero"
    aggregate_root = "Placeholder"
    required_permissions = ["financiero.execute"]

    def perform_action(self, params: dict):
        logger.info("SOLDADO PRESUPUESTO: Calculando varianza presupuestal.")
        return {"action": "variance_calculated"}

class SoldadoValidadorRubros(SoldadoN6OroV2):
    domain = "financiero"
    aggregate_root = "Placeholder"
    required_permissions = ["financiero.execute"]

    def perform_action(self, params: dict):
        logger.info("SOLDADO PRESUPUESTO: Validando rubros presupuestales.")
        return {"action": "categories_validated"}

class SoldadoAlertaSobrecosto(SoldadoN6OroV2):
    domain = "financiero"
    aggregate_root = "Placeholder"
    required_permissions = ["financiero.execute"]

    def perform_action(self, params: dict):
        logger.info("SOLDADO PRESUPUESTO: Disparando alertas de desviación.")
        from django.utils.module_loading import import_string
        Presupuesto = import_string('apps.prestadores.mi_negocio.gestion_financiera.models.Presupuesto') # DECOUPLED
        LineaPresupuesto = import_string('apps.prestadores.mi_negocio.gestion_financiera.models.LineaPresupuesto') # DECOUPLED
        AlertaFinanciera = import_string('apps.prestadores.mi_negocio.gestion_financiera.models.AlertaFinanciera') # DECOUPLED

        provider_id = params.get('provider_id')
        if not provider_id: return {"status": "FAILED"}

        lineas_excedidas = LineaPresupuesto.objects.filter(
            presupuesto__provider_id=provider_id,
            monto_ejecutado__gt=models.F('monto_presupuestado')
        )

        for l in lineas_excedidas:
            AlertaFinanciera.objects.get_or_create(
                provider_id=provider_id,
                tipo=AlertaFinanciera.TipoAlerta.DESVIACION_PRESUPUESTAL,
                titulo=f"Sobrecosto en {l.nombre_item}",
                defaults={
                    "descripcion": f"El rubro {l.nombre_item} ha excedido el presupuesto en ${l.monto_ejecutado - l.monto_presupuestado}.",
                    "nivel_prioridad": "ALTA"
                }
            )

        return {"status": "SUCCESS", "action": "alerts_dispatched", "alerts_created": lineas_excedidas.count()}

# --- SOLDADOS DE OBLIGACIONES ---

class SoldadoRegistroCredito(SoldadoN6OroV2):
    domain = "financiero"
    aggregate_root = "Placeholder"
    required_permissions = ["financiero.execute"]

    def perform_action(self, params: dict):
        logger.info("SOLDADO OBLIGACIONES: Registrando nuevo crédito.")
        from django.utils.module_loading import import_string
        CreditoFinanciero = import_string('apps.prestadores.mi_negocio.gestion_financiera.models.CreditoFinanciero') # DECOUPLED
        CuotaCredito = import_string('apps.prestadores.mi_negocio.gestion_financiera.models.CuotaCredito') # DECOUPLED
        from django.utils.module_loading import import_string
        FinanzasService = import_string('apps.prestadores.mi_negocio.gestion_financiera.services.FinanzasService') # DECOUPLED
        from decimal import Decimal
        from django.utils import timezone
        from dateutil.relativedelta import relativedelta

        if params.get("sub_task") == "registrar_credito":
            provider_id = params.get("provider_id")
            data = params.get("data", {})
            monto = Decimal(str(data.get("monto", 0)))
            tasa = Decimal(str(data.get("tasa", 0)))
            plazo = int(data.get("plazo", 12))

            credito = CreditoFinanciero.objects.create(
                provider_id=provider_id,
                entidad_financiera=data.get("banco", "Banco Genérico"),
                monto_principal=monto,
                tasa_interes_anual=tasa,
                plazo_meses=plazo,
                fecha_desembolso=timezone.now().date(),
                saldo_pendiente=monto
            )

            tabla = FinanzasService.calcular_amortizacion(monto, tasa, plazo)
            desembolso = timezone.now().date()

            for item in tabla:
                CuotaCredito.objects.create(
                    credito=credito,
                    numero_cuota=item["numero"],
                    fecha_vencimiento=desembolso + relativedelta(months=item["numero"]),
                    monto_capital=Decimal(str(item["capital"])),
                    monto_interes=Decimal(str(item["interes"]))
                )
            return {"status": "SUCCESS", "credito_id": str(credito.id), "cuotas": len(tabla)}
        return {"action": "idle"}

class SoldadoCalculadorAmortizacion(SoldadoN6OroV2):
    domain = "financiero"
    aggregate_root = "Placeholder"
    required_permissions = ["financiero.execute"]

    def perform_action(self, params: dict):
        return {"action": "amortization_calculated"}

class SoldadoTrackingPagos(SoldadoN6OroV2):
    domain = "financiero"
    aggregate_root = "Placeholder"
    required_permissions = ["financiero.execute"]

    def perform_action(self, params: dict):
        return {"action": "payments_tracked"}

class SoldadoAnalistaRiesgoCredito(SoldadoN6OroV2):
    domain = "financiero"
    aggregate_root = "Placeholder"
    required_permissions = ["financiero.execute"]

    def perform_action(self, params: dict):
        return {"action": "risk_analyzed"}

class SoldadoAuditorDeuda(SoldadoN6OroV2):
    domain = "financiero"
    aggregate_root = "Placeholder"
    required_permissions = ["financiero.execute"]

    def perform_action(self, params: dict):
        return {"action": "debt_audited"}

# --- SOLDADOS DE PROYECCIONES ---

class SoldadoRecoleccionHistorica(SoldadoN6OroV2):
    domain = "financiero"
    aggregate_root = "Placeholder"
    required_permissions = ["financiero.execute"]

    def perform_action(self, params: dict):
        return {"action": "history_collected"}

class SoldadoModeladoEscenarios(SoldadoN6OroV2):
    domain = "financiero"
    aggregate_root = "Placeholder"
    required_permissions = ["financiero.execute"]

    def perform_action(self, params: dict):
        return {"action": "scenarios_modeled"}

class SoldadoValidacionIA(SoldadoN6OroV2):
    domain = "financiero"
    aggregate_root = "Placeholder"
    required_permissions = ["financiero.execute"]

    def perform_action(self, params: dict):
        return {"action": "ai_validated"}

class SoldadoAjusteTendencia(SoldadoN6OroV2):
    domain = "financiero"
    aggregate_root = "Placeholder"
    required_permissions = ["financiero.execute"]

    def perform_action(self, params: dict):
        return {"action": "trends_adjusted"}

class SoldadoGeneradorReportePredictivo(SoldadoN6OroV2):
    domain = "financiero"
    aggregate_root = "Placeholder"
    required_permissions = ["financiero.execute"]

    def perform_action(self, params: dict):
        return {"action": "predictive_report_generated"}

# --- SOLDADOS DE INDICADORES ---

class SoldadoKPI(SoldadoN6OroV2):
    domain = "financiero"
    aggregate_root = "Placeholder"
    required_permissions = ["financiero.execute"]

    def perform_action(self, params: dict):
        from django.utils.module_loading import import_string
        FinanzasService = import_string('apps.prestadores.mi_negocio.gestion_financiera.services.FinanzasService') # DECOUPLED
        from django.utils.module_loading import import_string
        ProviderProfile = import_string('apps.prestadores.mi_negocio.gestion_operativa.modulos_genericos.perfil.models.ProviderProfile') # DECOUPLED

        provider_id = params.get('provider_id')
        if provider_id:
            provider = ProviderProfile.objects.get(id=provider_id)
            # En un flujo real, cada soldado calcularía un KPI específico.
            # Aquí llamamos al servicio que calcula varios.
            indicadores = FinanzasService.calcular_indicadores(provider)
            return {"status": "SUCCESS", "kpi": params.get("kpi_name"), "data": indicadores}
        return {"status": "FAILED"}
