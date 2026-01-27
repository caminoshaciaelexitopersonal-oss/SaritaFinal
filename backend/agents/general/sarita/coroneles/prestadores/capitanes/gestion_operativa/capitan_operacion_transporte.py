from .capitan_base import CapitanOperativaBase

class CapitanOperacionTransporte(CapitanOperativaBase):
    """
    Misión: Gestionar las operaciones específicas de los servicios de transporte.
    """
    def __init__(self, coronel):
        super().__init__(coronel, self.__doc__.strip())
