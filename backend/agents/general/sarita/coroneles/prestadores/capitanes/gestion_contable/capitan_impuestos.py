from backend.capitan_base import CapitanContableBase

class CapitanImpuestos(CapitanContableBase):
    """
    Misión: Garantizar el cumplimiento de todas las obligaciones fiscales, calculando y declarando impuestos de manera precisa y oportuna para evitar sanciones.
    """
    def __init__(self, coronel):
        super().__init__(coronel, self.__doc__.strip())
