from .capitan_base import CapitanSGSSTBase

class CapitanInspeccionesDeSeguridad(CapitanSGSSTBase):
    """
    Misión: Ejecución de inspecciones planeadas de áreas, equipos y EPP.
    """
    def __init__(self, coronel):
        super().__init__(coronel, self.__doc__.strip())
