from .capitan_base import CapitanContableBase

class CapitanInventarios(CapitanContableBase):
    """
    Misión: Supervisar y registrar los movimientos de inventario, asegurando la correcta valoración de existencias y el control de mermas.
    """
    def __init__(self, coronel):
        super().__init__(coronel, self.__doc__.strip())
