# backend/apps/sarita_agents/orchestrator.py

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
        Recibe una directiva de alto nivel, la valida y la delega.
        """
        print(f"GENERAL SARITA: Directiva recibida -> {directive}")

        domain = directive.get("domain")
        mission = directive.get("mission")

        if not domain or not mission:
            return self._report_error("La directiva debe contener 'domain' y 'mission'.")

        coronel = self.coroneles.get(domain)
        if not coronel:
            return self._report_error(f"No se encontró un Coronel para el dominio '{domain}'.")

        print(f"GENERAL SARITA: Delegando misión al Coronel de '{domain}'.")
        report = coronel.handle_mission(mission)

        return self._consolidate_report(report)

    def _report_error(self, message: str):
        print(f"GENERAL SARITA: Error en la directiva -> {message}")
        return {
            "status": "REJECTED",
            "message": message,
            "report_from": "General SARITA"
        }

    def _consolidate_report(self, report: dict):
        """
        Consolida el informe final del Coronel para la respuesta.
        """
        print("GENERAL SARITA: Misión completada. Informe final consolidado.")
        return {
            "status": "COMPLETED",
            "final_report": report,
            "report_from": "General SARITA"
        }

# Instancia única para ser usada en todo el sistema.
sarita_orchestrator = SaritaOrchestrator()
