from .capitan_base import CapitanOperativaBase

class CapitanOperacionArtesanos(CapitanOperativaBase):
    """
    Misión: Gestionar las operaciones específicas de los artesanos y sus productos.
    """
    def __init__(self, coronel):
        super().__init__(coronel, self.__doc__.strip())
