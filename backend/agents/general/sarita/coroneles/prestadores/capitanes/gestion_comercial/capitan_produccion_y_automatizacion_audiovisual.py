from backend.capitan_base import CapitanComercialBase

class CapitanProduccionYAutomatizacionAudiovisual(CapitanComercialBase):
    """
    Misión: Producir y automatizar el contenido audiovisual para marketing y ventas.
    """
    def __init__(self, coronel):
        super().__init__(coronel, self.__doc__.strip())
