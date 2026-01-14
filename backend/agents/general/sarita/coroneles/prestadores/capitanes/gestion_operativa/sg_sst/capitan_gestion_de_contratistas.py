from .capitan_base import CapitanSGSSTBase

class CapitanGestionDeContratistas(CapitanSGSSTBase):
    """
    Misión: Control y seguimiento de la seguridad y salud de terceros.
    """
    def __init__(self, coronel):
        super().__init__(coronel, self.__doc__.strip())
