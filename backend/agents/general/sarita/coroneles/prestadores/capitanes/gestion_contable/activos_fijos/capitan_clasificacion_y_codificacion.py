from .capitan_base import CapitanActivosFijosBase

class CapitanClasificacionYCodificacion(CapitanActivosFijosBase):
    """
    Misión: Asigna categorías, códigos únicos y centros de costo a los nuevos activos.
    """
    def __init__(self, coronel):
        super().__init__(coronel, self.__doc__.strip())
