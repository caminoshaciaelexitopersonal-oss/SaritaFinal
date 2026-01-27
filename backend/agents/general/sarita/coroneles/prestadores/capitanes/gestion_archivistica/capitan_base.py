from backend.capitan_base import CapitanBase

class CapitanArchivisticaBase(CapitanBase):
    """
    Clase base para los capitanes del módulo de Gestión Archivística.
    Hereda de CapitanBase para mantener la jerarquía y especialización del coronel.
    """
    def __init__(self, coronel, mision):
        super().__init__(coronel, mision)
