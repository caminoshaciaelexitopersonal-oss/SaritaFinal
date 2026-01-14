from ..capitan_base import CapitanBase

class CapitanOperativaBase(CapitanBase):
    """
    Clase base para los capitanes del módulo de Gestión Operativa.
    Hereda de CapitanBase para mantener la jerarquía y especialización del coronel.
    """
    def __init__(self, coronel, mision):
        super().__init__(coronel, mision)
