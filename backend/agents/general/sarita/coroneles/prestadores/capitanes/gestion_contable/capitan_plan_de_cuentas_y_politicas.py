from .capitan_base import CapitanContableBase

class CapitanPlanDeCuentasYPoliticas(CapitanContableBase):
    """
    Misión: Gestionar la estructura del Plan Único de Cuentas (PUC) y las políticas contables base de la entidad.
    """
    def __init__(self, coronel):
        super().__init__(coronel, self.__doc__.strip())
