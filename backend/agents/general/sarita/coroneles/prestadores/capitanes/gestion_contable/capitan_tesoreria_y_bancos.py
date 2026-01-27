from backend.capitan_base import CapitanContableBase

class CapitanTesoreriaYBancos(CapitanContableBase):
    """
    Misión: Gestionar los flujos de caja, realizar conciliaciones bancarias y controlar todos los movimientos de efectivo y equivalentes.
    """
    def __init__(self, coronel):
        super().__init__(coronel, self.__doc__.strip())
