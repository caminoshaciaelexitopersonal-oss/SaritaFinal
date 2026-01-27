from backend.capitan_base import CapitanNominaBase

class CapitanLiquidacionPrestacionesSociales(CapitanNominaBase):
    """
    Misión: Cálculo de primas, cesantías e intereses.
    """
    def __init__(self, coronel):
        super().__init__(coronel, self.__doc__.strip())
