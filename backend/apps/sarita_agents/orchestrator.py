# backend/apps/sarita_agents/orchestrator.py

import logging
 
from django.utils import timezone
from .models import Mision
from .agents.general.sarita.coroneles.prestadores.coronel import PrestadoresCoronel
from .agents.general.sarita.coroneles.administrador_general.coronel import AdministradorGeneralCoronel
from .marketing.coronel_marketing import CoronelMarketing
from .finanzas.coronel_finanzas import CoronelFinanzas
# from .agents.general.sarita.coroneles.clientes_turistas.coronel import ClientesTuristasCoronel
# from .agents.general.sarita.coroneles.gubernamental.coronel import GubernamentalCoronel

 
logger = logging.getLogger(__name__)
 

class SaritaOrchestrator:
    """
    El General SARITA.
    Punto de entrada único para todas las directivas.
    Interpreta la intención y delega la misión al Coronel apropiado.
    """

    def __init__(self):
        # El roster de Coroneles bajo el mando del General.
        # El 'domain' es la clave para la delegación.
        self.coroneles = {
            "prestadores": PrestadoresCoronel(general=self),
            "administrador_general": AdministradorGeneralCoronel(general=self),
            "marketing": CoronelMarketing(general=self, domain="marketing"),
            "finanzas": CoronelFinanzas(general=self, domain="finanzas"),
            # "clientes_turistas": ClientesTuristasCoronel(general=self),
            # "gubernamental": GubernamentalCoronel(general=self),
        }
 
        logger.info("GENERAL SARITA: Orquestador inicializado. Coroneles listos para recibir órdenes.")

    def start_mission(self, directive: dict, idempotency_key=None):
        """
        Punto de entrada para iniciar una nueva misión. Crea el registro y lo devuelve.
        """
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
        """
        Ejecuta la lógica de una misión que ya ha sido creada.
        """
        try:
            mision = Mision.objects.get(id=mision_id)
        except Mision.DoesNotExist:
            logger.error(f"CRITICAL: Misión con ID {mision_id} no encontrada para ejecutar.")
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

        # Simplemente delega. El Coronel y sus subordinados asíncronos se encargarán del resto.
        coronel.handle_mission(mision)

    def _report_error(self, message: str):
        logger.error(f"GENERAL SARITA: Error en la directiva -> {message}")
 
        return {
            "status": "REJECTED",
            "message": message,
            "report_from": "General SARITA"
        }

# Instancia única para ser usada en todo el sistema.
sarita_orchestrator = SaritaOrchestrator()
