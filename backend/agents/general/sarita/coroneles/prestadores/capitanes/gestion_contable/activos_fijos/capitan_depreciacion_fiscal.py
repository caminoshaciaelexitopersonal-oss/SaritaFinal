from backend.capitan_base import CapitanActivosFijosBase

class CapitanDepreciacionFiscal(CapitanActivosFijosBase):
    """
    Misión: Calcula la depreciación según las normativas fiscales locales (si es diferente).
    """
    def __init__(self, coronel):
        super().__init__(coronel, self.__doc__.strip())
