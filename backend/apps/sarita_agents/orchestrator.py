# backend/apps/sarita_agents/orchestrator.py

import logging
from django.utils import timezone
from apps.admin_plataforma.models import GovernancePolicy
from .models import Mision
from .agents.general.sarita.coroneles.prestadores.coronel import PrestadoresCoronel
from .agents.general.sarita.coroneles.operativo_general.coronel import CoronelOperativoGeneral
from .agents.general.sarita.coroneles.operativa_turistica.coronel import CoronelOperativaTuristica
from .agents.general.sarita.coroneles.administrador_general.coronel import AdministradorGeneralCoronel
from .agents.general.sarita.coroneles.contable.coronel import CoronelContable
from .agents.general.sarita.coroneles.financiero.coronel import CoronelFinanciero
from .marketing.coronel_marketing import CoronelMarketing
from .finanzas.coronel_finanzas import CoronelFinanzas
from .agents.general.sarita.coroneles.sg_sst.coronel import CoronelSST
from .agents.general.sarita.coroneles.nomina.coronel import CoronelNomina
from apps.peace_net.coronel import PeaceNetCoronel
from apps.wallet.agents.coronel import CoronelMonedero
from apps.delivery.agents.coronel import CoronelDelivery
from .agents.interop.coronel import CoronelInteroperabilidad
from .agents.general.sarita.coroneles.clientes_turistas.coronel import ClientesTuristasCoronel
from .agents.general.sarita.coroneles.gubernamental.coronel import GubernamentalCoronel

logger = logging.getLogger(__name__)

class SaritaOrchestrator:
    """
    El General SARITA.
    Punto de entrada único para todas las directivas.
    Interpreta la intención y delega la misión al Coronel apropiado.
    """

    def __init__(self):
        # El roster de Coroneles bajo el mando del General.
        op_turistica = CoronelOperativaTuristica(general=self)
        self.coroneles = {
            "prestadores": PrestadoresCoronel(general=self),
            "operativo_general": CoronelOperativoGeneral(general=self),
            "operativa_turistica": op_turistica,
            # Retrocompatibilidad de dominios especializados
            "operativo_hospedaje": op_turistica,
            "operativo_gastronomia": op_turistica,
            "operativo_transporte": op_turistica,
            "operativo_nocturno": op_turistica,
            "operativo_guias": op_turistica,
            "operativo_agencia": op_turistica,

            "administrador_general": AdministradorGeneralCoronel(general=self),
            "contabilidad": CoronelContable(general=self),
            "finanzas": CoronelFinanciero(general=self),
            "marketing": CoronelMarketing(general=self, domain="marketing"),
            "finanzas_marketing": CoronelFinanzas(general=self, domain="finanzas_marketing"),
            "sg_sst": CoronelSST(general=self, domain="sg_sst"),
            "nomina": CoronelNomina(general=self, domain="nomina"),
            "peace_net": PeaceNetCoronel(general=self, domain="peace_net"),
            "wallet": CoronelMonedero(general=self),
            "delivery": CoronelDelivery(general=self),
            "interop": CoronelInteroperabilidad(general=self),
            "clientes_turistas": ClientesTuristasCoronel(general=self),
            "gubernamental": GubernamentalCoronel(general=self),
        }
 
        logger.info("GENERAL SARITA: Orquestador inicializado. Coroneles listos para recibir órdenes.")

    def start_mission(self, directive: dict, idempotency_key=None):
        if idempotency_key and Mision.objects.filter(idempotency_key=idempotency_key).exists():
            raise ValueError("Directiva duplicada.")

        mision = Mision.objects.create(
            idempotency_key=idempotency_key,
            directiva_original=directive,
            dominio=directive.get("domain"),
            estado='EN_COLA'
        )
        return mision

    def execute_mission(self, mision_id: str):
        attack_mode = GovernancePolicy.objects.filter(name__in=["KILL_SWITCH_AGENTS", "SYSTEM_ATTACK_MODE"], is_active=True).exists()
        if attack_mode:
            logger.error(f"S-0: Misión {mision_id} RECHAZADA. Autonomía suspendida por estado de defensa.")
            return

        try:
            mision = Mision.objects.get(id=mision_id)
        except Mision.DoesNotExist:
            logger.error(f"CRITICAL: Misión con ID {mision_id} no encontrada para ejecutar.")
            return

        if not self._validate_mission_integrity(mision):
            mision.estado = 'FALLIDA'
            mision.resultado_final = {"error": "Fallo de integridad en la directiva de la misión."}
            mision.save()
            return

        logger.info(f"GENERAL SARITA: Ejecutando misión {mision.id}")
        mision.estado = 'EN_PROGRESO'
        mision.save()

        domain = mision.dominio
        coronel = self.coroneles.get(domain)

        if not coronel:
            mision.estado = 'FALLIDA'
            mision.resultado_final = {"error": f"No se encontró un Coronel para el dominio '{domain}'."}
            mision.timestamp_fin = timezone.now()
            mision.save()
            logger.error(f"Misión {mision.id} falló: No se encontró Coronel para el dominio '{domain}'.")
            return

        logger.info(f"GENERAL SARITA: Delegando misión {mision.id} al Coronel de '{domain}'.")
        coronel.handle_mission(mision)

    def handle_directive(self, directive: dict):
        mision = self.start_mission(directive)
        self.execute_mission(mision.id)
        mision.refresh_from_db()
        return mision.resultado_final or {"status": "EN_COLA", "mision_id": str(mision.id)}

    def _validate_mission_integrity(self, mision: Mision) -> bool:
        if mision.dominio != mision.directiva_original.get("domain"):
            logger.error(f"S-0: Violación de integridad detectada en misión {mision.id}.")
            return False
        return True

    def _report_error(self, message: str):
        logger.error(f"GENERAL SARITA: Error en la directiva -> {message}")
        return {
            "status": "REJECTED",
            "message": message,
            "report_from": "General SARITA"
        }

sarita_orchestrator = SaritaOrchestrator()
