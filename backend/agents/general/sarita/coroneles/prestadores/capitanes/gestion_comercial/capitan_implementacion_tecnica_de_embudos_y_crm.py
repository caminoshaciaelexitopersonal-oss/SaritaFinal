from .capitan_base import CapitanComercialBase

class CapitanImplementacionTecnicaDeEmbudosYCRM(CapitanComercialBase):
    """
    Misión: Implementar y mantener la infraestructura técnica de los embudos de venta y el CRM.
    """
    def __init__(self, coronel):
        super().__init__(coronel, self.__doc__.strip())
