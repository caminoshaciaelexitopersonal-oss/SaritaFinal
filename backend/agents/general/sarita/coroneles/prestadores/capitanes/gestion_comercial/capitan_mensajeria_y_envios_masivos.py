from .capitan_base import CapitanComercialBase

class CapitanMensajeriaYEnviosMasivos(CapitanComercialBase):
    """
    Misión: Gestionar las campañas de mensajería y envíos masivos (email, SMS, etc.).
    """
    def __init__(self, coronel):
        super().__init__(coronel, self.__doc__.strip())
