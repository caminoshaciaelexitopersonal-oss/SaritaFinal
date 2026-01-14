from .capitan_base import CapitanActivosFijosBase

class CapitanInventarioFisicoYTrazabilidad(CapitanActivosFijosBase):
    """
    Misión: Realiza inventarios periódicos, gestiona ubicaciones y responsables.
    """
    def __init__(self, coronel):
        super().__init__(coronel, self.__doc__.strip())
