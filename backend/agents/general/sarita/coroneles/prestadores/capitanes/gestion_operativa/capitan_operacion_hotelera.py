from backend.capitan_base import CapitanOperativaBase

class CapitanOperacionHotelera(CapitanOperativaBase):
    """
    Misión: Gestionar las operaciones específicas de los servicios hoteleros.
    """
    def __init__(self, coronel):
        super().__init__(coronel, self.__doc__.strip())
