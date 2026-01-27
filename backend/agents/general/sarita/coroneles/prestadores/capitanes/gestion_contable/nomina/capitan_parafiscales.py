from backend.capitan_base import CapitanNominaBase

class CapitanParafiscales(CapitanNominaBase):
    """
    Misión: Gestión y liquidación de los aportes parafiscales (SENA, ICBF y Cajas de Compensación Familiar).
    """
    def __init__(self, coronel):
        super().__init__(coronel, self.__doc__.strip())
