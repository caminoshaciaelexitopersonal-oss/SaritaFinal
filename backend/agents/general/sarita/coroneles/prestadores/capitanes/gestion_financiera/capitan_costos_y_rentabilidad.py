from backend.capitan_base import CapitanFinancieraBase

class CapitanCostosYRentabilidad(CapitanFinancieraBase):
    """
    Misión: Analizar los costos y la rentabilidad de los productos y servicios.
    """
    def __init__(self, coronel):
        super().__init__(coronel, self.__doc__.strip())
