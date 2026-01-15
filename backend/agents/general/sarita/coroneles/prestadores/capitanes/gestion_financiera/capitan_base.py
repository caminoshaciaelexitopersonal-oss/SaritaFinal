from ..capitan_base import CapitanBase

class CapitanFinancieraBase(CapitanBase):
    """
    Clase base para los capitanes del módulo de Gestión Financiera.
    Hereda de CapitanBase para mantener la jerarquía y especialización del coronel.
    """
    def __init__(self, coronel, mision):
        super().__init__(coronel, mision)
