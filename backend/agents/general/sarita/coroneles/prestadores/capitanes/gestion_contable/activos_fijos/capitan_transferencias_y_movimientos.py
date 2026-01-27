from backend.capitan_base import CapitanActivosFijosBase

class CapitanTransferenciasYMovimientos(CapitanActivosFijosBase):
    """
    Misión: Administra las transferencias de activos entre áreas o sucursales.
    """
    def __init__(self, coronel):
        super().__init__(coronel, self.__doc__.strip())
