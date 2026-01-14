from .capitan_base import CapitanActivosFijosBase

class CapitanRevalorizacionYDeterioro(CapitanActivosFijosBase):
    """
    Misión: Gestiona los ajustes al valor del activo por condiciones de mercado o daño.
    """
    def __init__(self, coronel):
        super().__init__(coronel, self.__doc__.strip())
