from .capitan_base import CapitanSGSSTBase

class CapitanIndicadoresYAnalitica(CapitanSGSSTBase):
    """
    Misión: Medición, seguimiento y reporte de todos los KPIs del sistema.
    """
    def __init__(self, coronel):
        super().__init__(coronel, self.__doc__.strip())
