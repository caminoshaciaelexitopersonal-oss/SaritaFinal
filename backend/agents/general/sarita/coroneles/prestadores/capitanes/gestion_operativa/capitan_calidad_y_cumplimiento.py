from .capitan_base import CapitanOperativaBase

class CapitanCalidadYCumplimiento(CapitanOperativaBase):
    """
    Misión: Asegurar la calidad de los servicios y el cumplimiento de los estándares.
    """
    def __init__(self, coronel):
        super().__init__(coronel, self.__doc__.strip())
