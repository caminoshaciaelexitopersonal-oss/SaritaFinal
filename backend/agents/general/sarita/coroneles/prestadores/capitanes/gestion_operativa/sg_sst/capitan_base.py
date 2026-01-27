from ..capitan_base import CapitanOperativaBase

class CapitanSGSSTBase(CapitanOperativaBase):
    """
    Clase base para los capitanes del módulo de SG-SST.
    Hereda de CapitanOperativaBase para mantener la jerarquía y especialización.
    """
    def __init__(self, coronel, mision):
        super().__init__(coronel, mision)
