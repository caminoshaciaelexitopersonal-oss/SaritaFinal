from backend.capitan_base import CapitanOperativaBase

class CapitanComunicacionesOperativas(CapitanOperativaBase):
    """
    Misión: Gestionar las comunicaciones operativas con clientes y personal.
    """
    def __init__(self, coronel):
        super().__init__(coronel, self.__doc__.strip())
