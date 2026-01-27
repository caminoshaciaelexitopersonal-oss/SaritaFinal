from backend.capitan_base import CapitanFinancieraBase

class CapitanContabilidadYEstadosFinancieros(CapitanFinancieraBase):
    """
    Misión: Gestionar la contabilidad y la generación de estados financieros.
    """
    def __init__(self, coronel):
        super().__init__(coronel, self.__doc__.strip())
