from backend.capitan_base import CapitanNominaBase

class CapitanControlTiemposYAsistencia(CapitanNominaBase):
    """
    Misión: Gestión de marcaciones, turnos y ausentismo.
    """
    def __init__(self, coronel):
        super().__init__(coronel, self.__doc__.strip())
