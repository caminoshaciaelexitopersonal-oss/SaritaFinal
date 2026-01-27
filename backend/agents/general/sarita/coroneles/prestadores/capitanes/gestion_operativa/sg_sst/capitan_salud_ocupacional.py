from backend.capitan_base import CapitanSGSSTBase

class CapitanSaludOcupacional(CapitanSGSSTBase):
    """
    Misión: Seguimiento a exámenes médicos y programas de vigilancia epidemiológica.
    """
    def __init__(self, coronel):
        super().__init__(coronel, self.__doc__.strip())
