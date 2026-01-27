from .capitan_base import CapitanContableBase

class CapitanCuentasPorPagar(CapitanContableBase):
    """
    Misión: Administrar y controlar todas las obligaciones y cuentas por pagar, asegurando pagos puntuales y manteniendo relaciones saludables con los proveedores.
    """
    def __init__(self, coronel):
        super().__init__(coronel, self.__doc__.strip())
