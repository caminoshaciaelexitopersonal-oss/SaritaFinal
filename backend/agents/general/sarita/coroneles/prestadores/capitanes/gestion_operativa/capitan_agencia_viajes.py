from .capitan_base import CapitanOperativaBase

class CapitanAgenciaViajes(CapitanOperativaBase):
    """
    Misión: Gestionar las operaciones específicas de las agencias de viajes.
    """
    def __init__(self, coronel):
        super().__init__(coronel, self.__doc__.strip())
