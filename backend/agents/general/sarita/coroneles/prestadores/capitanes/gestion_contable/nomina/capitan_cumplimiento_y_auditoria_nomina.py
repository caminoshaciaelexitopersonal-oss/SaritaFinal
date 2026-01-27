from .capitan_base import CapitanNominaBase

class CapitanCumplimientoYAuditoriaNomina(CapitanNominaBase):
    """
    Misión: Control de cambios, perfiles de seguridad y atención a requerimientos.
    """
    def __init__(self, coronel):
        super().__init__(coronel, self.__doc__.strip())
