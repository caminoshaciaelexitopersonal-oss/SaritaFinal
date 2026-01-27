from backend.capitan_base import CapitanNominaBase

class CapitanDeducciones(CapitanNominaBase):
    """
    Misión: Gestión de préstamos, embargos, aportes y otros descuentos.
    """
    def __init__(self, coronel):
        super().__init__(coronel, self.__doc__.strip())
