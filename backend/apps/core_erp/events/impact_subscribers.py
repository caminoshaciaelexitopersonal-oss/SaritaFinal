import logging
from decimal import Decimal
from django.utils import timezone
from apps.core_erp.event_bus import EventBus
from .erp_events import ErpImpactRequested

logger = logging.getLogger(__name__)

def handle_erp_impact(event: ErpImpactRequested):
    """
    Subscriber global (temporal) que distribuye el impacto a los dominios.
    REFACTORED FASE 1: Lógica restaurada con desacoplamiento dinámico.
    """
    logger.info(f"Handler: Procesando impacto ERP para {event.event_type}")
    payload = event.payload

    # Simulación de usuario (En un sistema real se recuperaría CustomUser.objects.get(id=event.user_id))
    user_id = event.user_id

    # 1. DIMENSIÓN COMERCIAL
    try:
        from django.utils.module_loading import import_string
        OperacionComercial = import_string('apps.prestadores.mi_negocio.gestion_comercial.domain.models.OperacionComercial') # DECOUPLED

        perfil_id = payload.get("perfil_id")
        cliente_id = payload.get("cliente_id")

        if perfil_id and cliente_id:
            OperacionComercial.objects.create(
                perfil_ref_id=perfil_id,
                cliente_ref_id=cliente_id,
                total=Decimal(str(payload.get("amount", 0))),
                estado="CONFIRMADA",
                tipo_operacion="VENTA"
            )
            logger.info("Impacto Comercial procesado (Decoupled)")
    except Exception as e:
        logger.warning(f"Fallo en Impacto Comercial Decoupled: {e}")

    # 2. DIMENSIÓN CONTABLE
    try:
        from django.utils.module_loading import import_string
        AsientoContable = import_string('apps.prestadores.mi_negocio.gestion_contable.contabilidad.models.AsientoContable') # DECOUPLED
        PeriodoContable = import_string('apps.prestadores.mi_negocio.gestion_contable.contabilidad.models.PeriodoContable') # DECOUPLED

        perfil_id = payload.get("perfil_id")
        if perfil_id:
            periodo = PeriodoContable.objects.filter(provider_id=perfil_id, cerrado=False).first()
            if periodo:
                AsientoContable.objects.create(
                    provider_id=perfil_id,
                    periodo=periodo,
                    date=timezone.now().date(),
                    description=f"Impacto Automático F1 - {event.event_type} - {payload.get('description', '')}"
                )
                logger.info("Impacto Contable procesado (Decoupled)")
    except Exception as e:
        logger.warning(f"Fallo en Impacto Contable Decoupled: {e}")

    # 3. DIMENSIÓN FINANCIERA
    try:
        if "wallet_transaction_id" in payload:
             logger.info(f"Vínculo financiero con transacción {payload['wallet_transaction_id']} detectado.")

        from django.utils.module_loading import import_string
        OrdenPago = import_string('apps.prestadores.mi_negocio.gestion_financiera.models.OrdenPago') # DECOUPLED

        perfil_id = payload.get("perfil_id")
        if event.event_type == "LIQUIDATION" and perfil_id:
            OrdenPago.objects.create(
                perfil_ref_id=perfil_id,
                amount=Decimal(str(payload.get("amount", 0))),
                payment_date=timezone.now().date(),
                concept=f"Liquidación Monedero - {event.event_type}",
                status="PENDIENTE"
            )
            logger.info("Impacto Financiero procesado (Decoupled)")
    except Exception as e:
        logger.warning(f"Fallo en Impacto Financiero Decoupled: {e}")

    # 4. DIMENSIÓN OPERATIVA
    try:
        if "delivery_service_id" in payload or "reserva_id" in payload:
            logger.info(f"Impacto Operativo detectado para {payload.get('delivery_service_id') or payload.get('reserva_id')}")
            # Aquí se podrían disparar notificaciones de despacho o actualización de estados
            logger.info("Impacto Operativo procesado (Decoupled)")
    except Exception as e:
        logger.warning(f"Fallo en Impacto Operativo Decoupled: {e}")

    # 5. DIMENSIÓN ANALÍTICA
    try:
        from django.utils.module_loading import import_string
        SaaSMetric = import_string('apps.operational_intelligence.models.SaaSMetric') # DECOUPLED

        amount = Decimal(str(payload.get("amount", 0)))
        if amount > 0:
            SaaSMetric.objects.create(
                metric_name="REVENUE_EVENT",
                value=amount,
                dimension=event.event_type,
                meta_data={"correlation_id": str(event.event_id)}
            )
            logger.info("Impacto Analítico procesado (Decoupled)")
    except Exception as e:
        logger.warning(f"Fallo en Impacto Analítico Decoupled: {e}")

# Registro de suscriptores
EventBus.subscribe("ERP_IMPACT_REQUESTED", handle_erp_impact)
