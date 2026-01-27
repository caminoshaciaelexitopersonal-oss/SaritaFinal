from backend.capitan_base import CapitanArchivisticaBase

class CapitanSeguridadDocumental(CapitanArchivisticaBase):
    """
    Misión: Garantizar la seguridad y el control de acceso a los documentos.
    """
    def __init__(self, coronel):
        super().__init__(coronel, self.__doc__.strip())
