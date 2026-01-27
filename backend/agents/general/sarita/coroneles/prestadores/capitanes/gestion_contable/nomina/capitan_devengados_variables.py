from backend.capitan_base import CapitanNominaBase

class CapitanDevengadosVariables(CapitanNominaBase):
    """
    Misión: Cálculo de horas extras, recargos, comisiones y bonos.
    """
    def __init__(self, coronel):
        super().__init__(coronel, self.__doc__.strip())
