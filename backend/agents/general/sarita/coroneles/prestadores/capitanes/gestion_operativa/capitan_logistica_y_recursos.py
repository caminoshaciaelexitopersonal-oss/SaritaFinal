from backend.capitan_base import CapitanOperativaBase

class CapitanLogisticaYRecursos(CapitanOperativaBase):
    """
    Misión: Coordinar la logística y la asignación de recursos para la prestación de servicios.
    """
    def __init__(self, coronel):
        super().__init__(coronel, self.__doc__.strip())
