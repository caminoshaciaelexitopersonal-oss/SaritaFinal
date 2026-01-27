from .capitan_base import CapitanActivosFijosBase

class CapitanSegurosYPolizas(CapitanActivosFijosBase):
    """
    Misión: Administra la información de los seguros que cubren los activos.
    """
    def __init__(self, coronel):
        super().__init__(coronel, self.__doc__.strip())
