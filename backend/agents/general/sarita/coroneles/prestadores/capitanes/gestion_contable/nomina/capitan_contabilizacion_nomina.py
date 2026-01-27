from .capitan_base import CapitanNominaBase

class CapitanContabilizacionNomina(CapitanNominaBase):
    """
    Misión: Generación de los asientos contables derivados de la nómina.
    """
    def __init__(self, coronel):
        super().__init__(coronel, self.__doc__.strip())
