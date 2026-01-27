from backend.capitan_base import CapitanSGSSTBase

class CapitanMatrizDePeligrosIPERC(CapitanSGSSTBase):
    """
    Misión: Identificación, valoración y planes de control de riesgos.
    """
    def __init__(self, coronel):
        super().__init__(coronel, self.__doc__.strip())
