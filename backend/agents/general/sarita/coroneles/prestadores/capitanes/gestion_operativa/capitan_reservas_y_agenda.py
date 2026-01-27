from .capitan_base import CapitanOperativaBase

class CapitanReservasYAgenda(CapitanOperativaBase):
    """
    Misión: Gestionar las reservas, la agenda y la disponibilidad de los servicios.
    """
    def __init__(self, coronel):
        super().__init__(coronel, self.__doc__.strip())
