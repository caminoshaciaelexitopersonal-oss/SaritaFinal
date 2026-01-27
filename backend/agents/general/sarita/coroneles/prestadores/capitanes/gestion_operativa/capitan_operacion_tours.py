from .capitan_base import CapitanOperativaBase

class CapitanOperacionTours(CapitanOperativaBase):
    """
    Misión: Gestionar las operaciones específicas de los tours y actividades turísticas.
    """
    def __init__(self, coronel):
        super().__init__(coronel, self.__doc__.strip())
