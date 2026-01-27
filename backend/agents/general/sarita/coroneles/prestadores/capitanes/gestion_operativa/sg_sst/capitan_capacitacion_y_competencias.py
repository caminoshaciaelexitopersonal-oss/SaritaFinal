from backend.capitan_base import CapitanSGSSTBase

class CapitanCapacitacionYCompetencias(CapitanSGSSTBase):
    """
    Misión: Gestión de la matriz de capacitación, inducciones y entrenamientos.
    """
    def __init__(self, coronel):
        super().__init__(coronel, self.__doc__.strip())
