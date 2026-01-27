from .capitan_base import CapitanNominaBase

class CapitanReportesYCertificados(CapitanNominaBase):
    """
    Misión: Emisión de desprendibles de pago, certificados laborales y reportes operativos.
    """
    def __init__(self, coronel):
        super().__init__(coronel, self.__doc__.strip())
