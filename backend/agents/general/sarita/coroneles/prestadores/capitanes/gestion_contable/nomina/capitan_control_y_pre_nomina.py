from .capitan_base import CapitanNominaBase

class CapitanControlYPreNomina(CapitanNominaBase):
    """
    Misión: Generación, validación y aprobación del borrador de la nómina.
    """
    def __init__(self, coronel):
        super().__init__(coronel, self.__doc__.strip())
