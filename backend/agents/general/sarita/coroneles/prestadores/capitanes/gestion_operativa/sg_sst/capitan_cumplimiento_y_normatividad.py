from .capitan_base import CapitanSGSSTBase

class CapitanCumplimientoYNormatividad(CapitanSGSSTBase):
    """
    Misión: Mantenimiento de la biblioteca legal y ejecución de auditorías internas.
    """
    def __init__(self, coronel):
        super().__init__(coronel, self.__doc__.strip())
