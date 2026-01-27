from backend.capitan_base import CapitanSGSSTBase

class CapitanInnovacionYTecnologia(CapitanSGSSTBase):
    """
    Misión: Implementación de nuevas tecnologías (apps, IoT, VR) para la gestión de SST.
    """
    def __init__(self, coronel):
        super().__init__(coronel, self.__doc__.strip())
