from .capitan_base import CapitanSGSSTBase

class CapitanInvestigacionDeAccidentes(CapitanSGSSTBase):
    """
    Misión: Registro e investigación de incidentes, accidentes y enfermedades laborales.
    """
    def __init__(self, coronel):
        super().__init__(coronel, self.__doc__.strip())
