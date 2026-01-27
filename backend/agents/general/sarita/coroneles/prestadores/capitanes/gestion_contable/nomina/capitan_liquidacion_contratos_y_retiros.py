from backend.capitan_base import CapitanNominaBase

class CapitanLiquidacionContratosYRetiros(CapitanNominaBase):
    """
    Misión: Procesamiento de liquidaciones finales e indemnizaciones.
    """
    def __init__(self, coronel):
        super().__init__(coronel, self.__doc__.strip())
