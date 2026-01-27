from backend.capitan_base import CapitanNominaBase

class CapitanLiquidacionSeguridadSocialPILA(CapitanNominaBase):
    """
    Misión: Generación y pago de la planilla de aportes.
    """
    def __init__(self, coronel):
        super().__init__(coronel, self.__doc__.strip())
