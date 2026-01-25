# backend/apps/sarita_agents/agents/general/sarita/coroneles/prestadores/coronel.py

from .....coronel_template import CoronelTemplate
# Importar los capitanes específicos de este dominio.
from .capitanes.dummy_capitan import DummyCapitan

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
            "dummy": DummyCapitan(coronel=self),
        }
