from .capitan_base import CapitanContableBase

class CapitanCostos(CapitanContableBase):
    """
    Misión: Analizar y controlar los costos operativos y de servicios, proporcionando información clave para la toma de decisiones y la optimización de recursos.
    """
    def __init__(self, coronel):
        super().__init__(coronel, self.__doc__.strip())
