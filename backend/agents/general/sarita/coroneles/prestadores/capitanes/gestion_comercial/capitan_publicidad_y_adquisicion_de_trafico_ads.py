from backend.capitan_base import CapitanComercialBase

class CapitanPublicidadYAdquisicionDeTraficoADS(CapitanComercialBase):
    """
    Misión: Gestionar las campañas de publicidad pagada y la adquisición de tráfico.
    """
    def __init__(self, coronel):
        super().__init__(coronel, self.__doc__.strip())
