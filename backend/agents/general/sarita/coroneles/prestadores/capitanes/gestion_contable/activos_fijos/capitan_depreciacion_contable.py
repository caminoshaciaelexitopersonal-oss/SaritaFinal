from .capitan_base import CapitanActivosFijosBase

class CapitanDepreciacionContable(CapitanActivosFijosBase):
    """
    Misión: Calcula y registra la depreciación según las políticas de la empresa (NIIF).
    """
    def __init__(self, coronel):
        super().__init__(coronel, self.__doc__.strip())
