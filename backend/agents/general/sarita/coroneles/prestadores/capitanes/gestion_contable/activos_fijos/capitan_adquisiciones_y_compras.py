from .capitan_base import CapitanActivosFijosBase

class CapitanAdquisicionesYCompras(CapitanActivosFijosBase):
    """
    Misión: Gestiona la compra y el proceso de alta inicial de los activos.
    """
    def __init__(self, coronel):
        super().__init__(coronel, self.__doc__.strip())
