from .capitan_base import CapitanFinancieraBase

class CapitanControlFinanciero(CapitanFinancieraBase):
    """
    Misión: Supervisar y controlar las finanzas del negocio.
    """
    def __init__(self, coronel):
        super().__init__(coronel, self.__doc__.strip())
