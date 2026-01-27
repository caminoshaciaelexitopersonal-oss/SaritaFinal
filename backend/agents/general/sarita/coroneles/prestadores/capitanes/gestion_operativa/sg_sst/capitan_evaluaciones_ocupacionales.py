from .capitan_base import CapitanSGSSTBase

class CapitanEvaluacionesOcupacionales(CapitanSGSSTBase):
    """
    Misión: Gestión de evaluaciones ergonómicas, psicosociales y mediciones higiénicas.
    """
    def __init__(self, coronel):
        super().__init__(coronel, self.__doc__.strip())
