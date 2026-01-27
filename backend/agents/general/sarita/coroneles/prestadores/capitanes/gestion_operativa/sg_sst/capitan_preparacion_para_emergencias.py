from backend.capitan_base import CapitanSGSSTBase

class CapitanPreparacionParaEmergencias(CapitanSGSSTBase):
    """
    Misión: Gestión de planes de emergencia, brigadas y simulacros.
    """
    def __init__(self, coronel):
        super().__init__(coronel, self.__doc__.strip())
