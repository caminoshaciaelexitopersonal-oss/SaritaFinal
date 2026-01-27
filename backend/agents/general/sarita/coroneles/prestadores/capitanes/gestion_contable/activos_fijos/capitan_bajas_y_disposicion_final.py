from .capitan_base import CapitanActivosFijosBase

class CapitanBajasYDisposicionFinal(CapitanActivosFijosBase):
    """
    Misión: Administra el proceso completo de dar de baja un activo, ya sea por venta, obsolescencia o siniestro.
    """
    def __init__(self, coronel):
        super().__init__(coronel, self.__doc__.strip())
