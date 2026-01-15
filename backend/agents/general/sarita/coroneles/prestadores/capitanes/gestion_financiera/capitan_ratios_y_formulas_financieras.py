from .capitan_base import CapitanFinancieraBase

class CapitanRatiosYFormulasFinancieras(CapitanFinancieraBase):
    """
    Misión: Calcular y analizar ratios y fórmulas financieras para la toma de decisiones.
    """
    def __init__(self, coronel):
        super().__init__(coronel, self.__doc__.strip())
