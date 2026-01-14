from .capitan_base import CapitanContableBase

class CapitanFacturacion(CapitanContableBase):
    """
    Misión: Gestionar la emisión, envío y seguimiento de facturas de venta, asegurando la correcta facturación de todos los servicios prestados.
    """
    def __init__(self, coronel):
        super().__init__(coronel, self.__doc__.strip())
