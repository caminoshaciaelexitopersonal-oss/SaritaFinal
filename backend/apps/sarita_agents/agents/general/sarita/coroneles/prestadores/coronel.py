# backend/apps/sarita_agents/agents/general/sarita/coroneles/prestadores/coronel.py

from .....coronel_template import CoronelTemplate
# Importar los capitanes específicos de este dominio.
from .capitanes.onboarding_prestador_capitan import CapitanOnboardingPrestador

class PrestadoresCoronel(CoronelTemplate):
    """
    Coronel para el dominio de Prestadores.
    Gestiona todas las misiones relacionadas con proveedores de servicios.
    """
    def __init__(self, general):
        super().__init__(general=general, domain="prestadores")

    def _get_capitanes(self) -> dict:
        """
        Carga y devuelve el roster de Capitanes bajo el mando de este Coronel.
        """
        return {
            "onboarding": CapitanOnboardingPrestador(coronel=self),
        }

    def _select_capitan(self, directiva: dict):
        """
        Lógica para seleccionar el Capitán más adecuado para la misión.
        Para la Fase U, asumimos que cualquier misión de 'prestadores' es para onboarding.
        """
        mission_info = directiva.get("mission", {})
        mission_type = mission_info.get("type")

        if mission_type == "ONBOARDING_PRESTADOR":
            return self.capitanes.get("onboarding")

        return None # No se encontró capitán para esta misión
