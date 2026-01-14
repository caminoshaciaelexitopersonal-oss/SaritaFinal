from .capitan_base import CapitanContableBase

class CapitanConciliacionesBancarias(CapitanContableBase):
    """
    Misión: Realizar conciliaciones bancarias periódicas para asegurar que los registros contables coincidan con los extractos bancarios, identificando y resolviendo discrepancias.
    """
    def __init__(self, coronel):
        super().__init__(coronel, self.__doc__.strip())
