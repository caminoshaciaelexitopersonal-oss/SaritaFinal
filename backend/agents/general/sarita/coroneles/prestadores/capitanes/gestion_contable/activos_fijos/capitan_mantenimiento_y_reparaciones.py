from backend.capitan_base import CapitanActivosFijosBase

class CapitanMantenimientoYReparaciones(CapitanActivosFijosBase):
    """
    Misión: Registra y controla los costos de mantenimiento asociados a cada activo.
    """
    def __init__(self, coronel):
        super().__init__(coronel, self.__doc__.strip())
