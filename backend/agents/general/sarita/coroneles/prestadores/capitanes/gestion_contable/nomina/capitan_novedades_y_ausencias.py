from backend.capitan_base import CapitanNominaBase

class CapitanNovedadesYAusencias(CapitanNominaBase):
    """
    Misión: Procesamiento centralizado de incapacidades, licencias y vacaciones.
    """
    def __init__(self, coronel):
        super().__init__(coronel, self.__doc__.strip())
