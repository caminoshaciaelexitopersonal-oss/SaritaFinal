from backend.capitan_base import CapitanComercialBase

class CapitanGestionOperativaDeContenidosComerciales(CapitanComercialBase):
    """
    Misión: Gestionar la operación diaria de los contenidos comerciales en las diferentes plataformas.
    """
    def __init__(self, coronel):
        super().__init__(coronel, self.__doc__.strip())
