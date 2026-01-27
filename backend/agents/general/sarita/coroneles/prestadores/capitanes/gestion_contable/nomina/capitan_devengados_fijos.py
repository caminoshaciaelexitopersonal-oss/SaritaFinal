from backend.capitan_base import CapitanNominaBase

class CapitanDevengadosFijos(CapitanNominaBase):
    """
    Misión: Cálculo de salarios básicos, auxilios y pagos fijos recurrentes.
    """
    def __init__(self, coronel):
        super().__init__(coronel, self.__doc__.strip())
