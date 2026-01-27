from backend.capitan_base import CapitanOperativaBase

class CapitanOperacionesGenerales(CapitanOperativaBase):
    """
    Misión: Supervisar y coordinar las operaciones generales del negocio.
    """
    def __init__(self, coronel):
        super().__init__(coronel, self.__doc__.strip())
