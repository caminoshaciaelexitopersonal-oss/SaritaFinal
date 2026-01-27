from backend.capitan_base import CapitanArchivisticaBase

class CapitanCapturaYCreacionDocumental(CapitanArchivisticaBase):
    """
    Misión: Gestionar la captura y creación de documentos.
    """
    def __init__(self, coronel):
        super().__init__(coronel, self.__doc__.strip())
