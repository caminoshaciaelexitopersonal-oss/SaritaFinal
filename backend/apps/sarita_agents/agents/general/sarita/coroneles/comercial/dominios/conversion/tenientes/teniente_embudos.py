# backend/apps/sarita_agents/agents/general/sarita/coroneles/comercial/dominios/conversion/tenientes/teniente_embudos.py

from .......teniente_template import TenienteTemplate
from ..sargentos.sargento_validacion_precio import SargentoValidacionPrecio

class TenienteEmbudos(TenienteTemplate):
    """
    Teniente de Embudos.
    Planifica la conversión de un lead a través de los pasos del funnel.
    """
    def perform_action(self, parametros: dict) -> dict:
        # El Teniente coordina a los Sargentos
        sargento_precio = SargentoValidacionPrecio(teniente=self)

        # 1. Validar Precio de la Oferta en el Funnel
        validacion = sargento_precio.execute({
            "precio": parametros.get("valor_oferta"),
            "min_allowed": 10000,
            "max_allowed": 5000000
        })

        if validacion["status"] == "ERROR":
            return validacion

        # 2. Registrar evento de avance (Llamaría a otro sargento en un flujo real)
        return {
            "status": "CONVERSION_STEP_READY",
            "message": "Lead listo para avanzar en el embudo.",
            "data": validacion["data"]
        }
