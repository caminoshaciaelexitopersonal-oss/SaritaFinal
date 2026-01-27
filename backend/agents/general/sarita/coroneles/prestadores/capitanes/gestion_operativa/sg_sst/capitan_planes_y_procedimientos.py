from backend.capitan_base import CapitanSGSSTBase

class CapitanPlanesYProcedimientos(CapitanSGSSTBase):
    """
    Misión: Elaboración de planes de trabajo, procedimientos de tareas críticas (PETS) y permisos de trabajo de alto riesgo (PTAR).
    """
    def __init__(self, coronel):
        super().__init__(coronel, self.__doc__.strip())
