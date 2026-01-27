from backend.capitan_base import CapitanContableBase

class CapitanActivosFijosBase(CapitanContableBase):
    """
    Clase base para los capitanes del módulo de Activos Fijos.
    Hereda de CapitanContableBase para mantener la jerarquía y especialización.
    """
    def __init__(self, coronel, mision):
        super().__init__(coronel, mision)
