from backend.capitan_base import CapitanContableBase

class CapitanNomina(CapitanContableBase):
    """
    Misión: Administrar el proceso de nómina, asegurando el cálculo correcto y pago puntual de salarios, deducciones y beneficios a los empleados.
    """
    def __init__(self, coronel):
        super().__init__(coronel, self.__doc__.strip())
