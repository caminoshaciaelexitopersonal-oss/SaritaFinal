# backend/apps/sarita_agents/agents/coronel_template.py

class CoronelTemplate:
    """
    Plantilla base para todos los Coroneles.
    Define la interfaz y estructura común.
    """
    def __init__(self, general, domain: str):
        self.general = general
        self.domain = domain
        self.capitanes = self._get_capitanes()
        print(f"CORONEL ({self.domain}): Inicializado. Capitanes listos.")

    def handle_mission(self, mission: dict):
        """
        Recibe una misión del General, la descompone y la asigna a un Capitán.
        """
        print(f"CORONEL ({self.domain}): Misión recibida -> {mission}")

        # Lógica de enrutamiento para seleccionar el capitán adecuado.
        # Por ahora, se asume una lógica simple.
        capitan_asignado = self._select_capitan(mission)

        if not capitan_asignado:
            return self._report_error("No se pudo asignar un Capitán para esta misión.")

        print(f"CORONEL ({self.domain}): Asignando orden al Capitán '{capitan_asignado.__class__.__name__}'.")
        report = capitan_asignado.handle_order(mission)

        return self._package_report(report)

    def _get_capitanes(self) -> dict:
        """
        Carga los capitanes bajo el mando de este Coronel.
        Este método debe ser implementado por cada subclase de Coronel.
        """
        raise NotImplementedError("El método _get_capitanes() debe ser implementado por cada Coronel.")

    def _select_capitan(self, mission: dict):
        """
        Lógica para seleccionar el Capitán más adecuado para la misión.
        """
        # Por defecto, se selecciona el primer capitán disponible.
        # Esta lógica se puede hacer más sofisticada.
        if self.capitanes:
            return next(iter(self.capitanes.values()))
        return None

    def _report_error(self, message: str):
        return {
            "status": "FAILED",
            "message": message,
            "report_from": f"Coronel ({self.domain})"
        }

    def _package_report(self, report: dict):
        """
        Empaqueta el informe del Capitán antes de enviarlo al General.
        """
        return {
            "status": "FORWARDED",
            "captain_report": report,
            "report_from": f"Coronel ({self.domain})"
        }
