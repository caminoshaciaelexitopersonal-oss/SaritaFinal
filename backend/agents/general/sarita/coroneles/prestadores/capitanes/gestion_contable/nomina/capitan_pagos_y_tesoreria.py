from backend.capitan_base import CapitanNominaBase

class CapitanPagosYTesoreria(CapitanNominaBase):
    """
    Misión: Generación de archivos planos para bancos y control de la dispersión de pagos.
    """
    def __init__(self, coronel):
        super().__init__(coronel, self.__doc__.strip())
