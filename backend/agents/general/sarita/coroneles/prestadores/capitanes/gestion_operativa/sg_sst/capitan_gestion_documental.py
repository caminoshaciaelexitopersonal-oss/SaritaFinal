from .capitan_base import CapitanSGSSTBase

class CapitanGestionDocumental(CapitanSGSSTBase):
    """
    Misión: Control maestro de políticas, manuales, formatos y registros.
    """
    def __init__(self, coronel):
        super().__init__(coronel, self.__doc__.strip())
