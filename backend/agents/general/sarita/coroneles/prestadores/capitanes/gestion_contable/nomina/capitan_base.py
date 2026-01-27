from backend.capitan_base import CapitanContableBase

class CapitanNominaBase(CapitanContableBase):
    """
    Clase base para los capitanes del módulo de Nómina.
    Hereda de CapitanContableBase para mantener la jerarquía y especialización.
    """
    def __init__(self, coronel, mision):
        super().__init__(coronel, mision)
