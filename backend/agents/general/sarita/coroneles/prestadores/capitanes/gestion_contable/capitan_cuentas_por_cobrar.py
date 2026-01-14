from .capitan_base import CapitanContableBase

class CapitanCuentasPorCobrar(CapitanContableBase):
    """
    Misión: Gestionar y monitorear todas las cuentas por cobrar, optimizando el flujo de caja mediante el seguimiento proactivo de facturas y pagos pendientes.
    """
    def __init__(self, coronel):
        super().__init__(coronel, self.__doc__.strip())
