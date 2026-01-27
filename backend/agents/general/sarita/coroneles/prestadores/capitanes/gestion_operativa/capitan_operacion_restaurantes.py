from backend.capitan_base import CapitanOperativaBase

class CapitanOperacionRestaurantes(CapitanOperativaBase):
    """
    Misión: Gestionar las operaciones específicas de los restaurantes y servicios de alimentos.
    """
    def __init__(self, coronel):
        super().__init__(coronel, self.__doc__.strip())
