from backend.capitan_base import CapitanContableBase

class CapitanActivosFijos(CapitanContableBase):
    """
    Misión: Controlar y gestionar el ciclo de vida completo de los activos fijos, desde la adquisición hasta la baja, incluyendo el cálculo de la depreciación.
    """
    def __init__(self, coronel):
        super().__init__(coronel, self.__doc__.strip())
