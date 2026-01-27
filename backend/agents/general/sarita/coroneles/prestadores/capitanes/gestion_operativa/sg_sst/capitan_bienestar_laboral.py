from backend.capitan_base import CapitanSGSSTBase

class CapitanBienestarLaboral(CapitanSGSSTBase):
    """
    Misión: Desarrollo de programas de salud mental, pausas activas y prevención del acoso.
    """
    def __init__(self, coronel):
        super().__init__(coronel, self.__doc__.strip())
