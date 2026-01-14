from .capitan_base import CapitanContableBase

class CapitanLibroDiarioYMayor(CapitanContableBase):
    """
    Misión: Registrar y centralizar todas las transacciones contables en los libros principales, asegurando la consistencia y trazabilidad.
    """
    def __init__(self, coronel):
        super().__init__(coronel, self.__doc__.strip())
