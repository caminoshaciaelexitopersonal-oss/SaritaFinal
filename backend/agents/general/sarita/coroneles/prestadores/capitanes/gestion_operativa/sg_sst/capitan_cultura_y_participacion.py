from backend.capitan_base import CapitanSGSSTBase

class CapitanCulturaYParticipacion(CapitanSGSSTBase):
    """
    Misión: Administración del COPASST, campañas de seguridad y programas de liderazgo.
    """
    def __init__(self, coronel):
        super().__init__(coronel, self.__doc__.strip())
