from .capitan_base import CapitanContableBase

class CapitanPeriodosContables(CapitanContableBase):
    """
    Misión: Controlar la apertura, cierre y bloqueo de periodos contables para garantizar la integridad de la información.
    """
    def __init__(self, coronel):
        super().__init__(coronel, self.__doc__.strip())
