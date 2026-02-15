import logging
from apps.sarita_agents.agents.teniente_template import TenienteTemplate
from apps.prestadores.mi_negocio.gestion_operativa.sargentos_especializados import SargentoEspecializado

logger = logging.getLogger(__name__)

# Instancia compartida de sargento (singleton pattern simbólico)
sargento_especializado = SargentoEspecializado()

class TenienteOperativoHospedaje(TenienteTemplate):
    def perform_action(self, parametros: dict):
        habitacion_id = parametros.get("habitacion_id")
        nuevo_estado = parametros.get("nuevo_estado")
        provider_id = parametros.get("provider_id")

        logger.info(f"TENIENTE HOSPEDAJE: Solicitando actualización para Hab {habitacion_id} -> {nuevo_estado} (Provider: {provider_id})")

        exito = sargento_especializado.actualizar_estado_habitacion(
            provider_id=provider_id,
            habitacion_id=habitacion_id,
            nuevo_estado=nuevo_estado
        )

        if exito:
            return {"status": "SUCCESS", "entity": "Room", "id": habitacion_id}
        else:
            raise Exception(f"Sargento no pudo completar la acción para Habitación {habitacion_id}")

class TenienteOperativoGastronomia(TenienteTemplate):
    def perform_action(self, parametros: dict):
        mesa_id = parametros.get("mesa_id")
        accion = parametros.get("accion", "ORDER")
        logger.info(f"TENIENTE GASTRONOMIA: Ejecutando {accion} para Mesa {mesa_id}")
        return {"status": "SUCCESS", "entity": "RestaurantTable", "id": mesa_id}

class TenienteOperativoTransporte(TenienteTemplate):
    def perform_action(self, parametros: dict):
        vehiculo_id = parametros.get("vehiculo_id")
        ruta_id = parametros.get("ruta_id")
        logger.info(f"TENIENTE TRANSPORTE: Despachando {vehiculo_id} en ruta {ruta_id}")
        return {"status": "SUCCESS", "entity": "Vehicle", "id": vehiculo_id}
