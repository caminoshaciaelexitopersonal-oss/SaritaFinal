# backend/apps/sarita_agents/orchestrator.py

from django.utils import timezone
from .models import Mision
from .agents.general.sarita.coroneles.prestadores.coronel import PrestadoresCoronel
# Import other Colonels as they are created
# from .agents.general.sarita.coroneles.administrador_general.coronel import AdministradorGeneralCoronel
# from .agents.general.sarita.coroneles.clientes_turistas.coronel import ClientesTuristasCoronel
# from .agents.general.sarita.coroneles.gubernamental.coronel import GubernamentalCoronel


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
            # "administrador_general": AdministradorGeneralCoronel(general=self),
            # "clientes_turistas": ClientesTuristasCoronel(general=self),
            # "gubernamental": GubernamentalCoronel(general=self),
        }
        print("GENERAL SARITA: Orquestador inicializado. Coroneles listos para recibir órdenes.")

    def handle_directive(self, directive: dict):
        """
        Recibe una directiva de alto nivel, la valida, la persiste y la delega.
        """
        print(f"GENERAL SARITA: Directiva recibida -> {directive}")

        domain = directive.get("domain")
        if not domain:
            return self._report_error("La directiva debe contener un 'domain'.")

        # 1. Crear el registro de la Misión
        mision = Mision.objects.create(
            directiva_original=directive,
            dominio=domain,
            estado='EN_PROGRESO'
        )

        coronel = self.coroneles.get(domain)
        if not coronel:
            mision.estado = 'FALLIDA'
            mision.resultado_final = {"error": f"No se encontró un Coronel para el dominio '{domain}'."}
            mision.timestamp_fin = timezone.now()
            mision.save()
            return mision.resultado_final

        print(f"GENERAL SARITA: Delegando misión {mision.id} al Coronel de '{domain}'.")

        try:
            # 2. Delegar al Coronel
            reporte = coronel.handle_mission(mision) # Pasa el objeto Mision completo

            # 3. Actualizar y finalizar la Misión
            mision.resultado_final = reporte
            mision.estado = 'COMPLETADA'
            print(f"GENERAL SARITA: Misión {mision.id} completada con éxito.")

        except Exception as e:
            mision.estado = 'FALLIDA'
            mision.resultado_final = {"error": f"Error durante la ejecución de la misión: {str(e)}"}
            print(f"GENERAL SARITA: Misión {mision.id} falló.")

        mision.timestamp_fin = timezone.now()
        mision.save()

        return mision.resultado_final

    def _report_error(self, message: str):
        print(f"GENERAL SARITA: Error en la directiva -> {message}")
        return {
            "status": "REJECTED",
            "message": message,
            "report_from": "General SARITA"
        }

# Instancia única para ser usada en todo el sistema.
sarita_orchestrator = SaritaOrchestrator()
