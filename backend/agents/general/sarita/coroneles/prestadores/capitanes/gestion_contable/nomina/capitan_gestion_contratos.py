from .capitan_base import CapitanNominaBase

class CapitanGestionContratos(CapitanNominaBase):
    """
    Misión: Administración del ciclo de vida de los contratos y sus condiciones.
    """
    def __init__(self, coronel):
        super().__init__(coronel, self.__doc__.strip())
