from backend.capitan_base import CapitanNominaBase

class CapitanDatosMaestrosEmpleados(CapitanNominaBase):
    """
    Misión: Creación y mantenimiento del maestro de empleados.
    """
    def __init__(self, coronel):
        super().__init__(coronel, self.__doc__.strip())
