"""
Agente Capitán Táctico: CapitanMarketing

Responsable de ejecutar tareas atómicas relacionadas con marketing,
promociones, descuentos y campañas.
"""

from typing import Dict, Any, List
import uuid

# Simulación de una base de datos de promociones en memoria.
PROMOCIONES_DB = {}

class CapitanMarketing:
    """
    Ejecuta tareas tácticas de marketing asignadas por un Coronel.
    """

    def execute_task(self, task_payload: Dict[str, Any]) -> Dict[str, Any]:
        """
        Punto de entrada principal que enruta la tarea al método correcto.
        """
        task_type = task_payload.get("type")
        print(f"CAPITAN MARKETING: Recibida tarea táctica '{task_type}'.")

        handler_method = getattr(self, f"_handle_{task_type}", self._handle_unknown)
        return handler_method(task_payload)

    def _handle_crear_promocion(self, task_data: Dict[str, Any]) -> Dict[str, Any]:
        """
        Lógica para crear una nueva promoción o descuento.
        """
        datos_promo = task_data.get("datos_promocion", {})
        nombre = datos_promo.get("nombre")
        tipo = datos_promo.get("tipo", "PORCENTAJE") # PORCENTAJE o MONTO_FIJO
        valor = datos_promo.get("valor")

        if not nombre or valor is None:
            return {"status": "FAILED", "error": "Datos incompletos. Se requiere nombre, tipo y valor."}

        print(f"CAPITAN MARKETING: Creando promoción '{nombre}' ({tipo}: {valor}).")

        promo_id = f"PROMO-{uuid.uuid4().hex[:6].upper()}"
        PROMOCIONES_DB[promo_id] = {
            "id": promo_id,
            "nombre": nombre,
            "tipo": tipo,
            "valor": float(valor),
            "productos_asociados": []
        }

        return {
            "status": "COMPLETED",
            "result": {"promocion_id": promo_id, "mensaje": "Promoción creada exitosamente."}
        }

    def _handle_asociar_promo_a_producto(self, task_data: Dict[str, Any]) -> Dict[str, Any]:
        """
        Asocia una promoción existente a uno o más productos.
        """
        promo_id = task_data.get("promocion_id")
        producto_ids = task_data.get("producto_ids", [])

        if not promo_id or promo_id not in PROMOCIONES_DB:
            return {"status": "FAILED", "error": f"Promoción con ID '{promo_id}' no encontrada."}

        print(f"CAPITAN MARKETING: Asociando promoción '{promo_id}' a los productos: {producto_ids}.")

        # En una implementación real, se validaría que los productos existan.
        for prod_id in producto_ids:
            if prod_id not in PROMOCIONES_DB[promo_id]["productos_asociados"]:
                PROMOCIONES_DB[promo_id]["productos_asociados"].append(prod_id)

        return {
            "status": "COMPLETED",
            "result": {"promocion_id": promo_id, "mensaje": "Asociación completada."}
        }

    def _handle_enviar_campana_marketing(self, task_data: Dict[str, Any]) -> Dict[str, Any]:
        """
        Simula el envío de una campaña de marketing a una lista de clientes.
        """
        lista_clientes_ids = task_data.get("lista_clientes", [])
        mensaje = task_data.get("mensaje")

        if not lista_clientes_ids or not mensaje:
            return {"status": "FAILED", "error": "Se requiere una lista de clientes y un mensaje."}

        print(f"CAPITAN MARKETING: Iniciando envío de campaña a {len(lista_clientes_ids)} clientes.")

        for cliente_id in lista_clientes_ids:
            # Simulación de envío
            print(f"  -> Enviando a cliente '{cliente_id}': '{mensaje}'")

        return {
            "status": "COMPLETED",
            "result": {"clientes_notificados": len(lista_clientes_ids), "mensaje": "Campaña enviada."}
        }

    def _handle_unknown(self, task_data: Dict[str, Any]) -> Dict[str, Any]:
        """Maneja tareas desconocidas para este capitán."""
        task_type = task_data.get("type")
        return {
            "status": "FAILED",
            "error": f"El CapitanMarketing no puede manejar la tarea de tipo '{task_type}'."
        }

# Ejemplo de uso
if __name__ == '__main__':
    capitan = CapitanMarketing()

    # 1. Crear una promoción
    tarea_crear = {
        "type": "crear_promocion",
        "datos_promocion": {"nombre": "Descuento Verano 2024", "tipo": "PORCENTAJE", "valor": 15}
    }
    resultado_crear = capitan.execute_task(tarea_crear)
    print("Resultado Crear:", resultado_crear)

    print("\nBD de Promociones:", PROMOCIONES_DB)
    print("-" * 20)

    # 2. Asociar la promo a productos
    promo_id = resultado_crear.get("result", {}).get("promocion_id")
    tarea_asociar = {
        "type": "asociar_promo_a_producto",
        "promocion_id": promo_id,
        "producto_ids": ["PROD-ABC", "PROD-XYZ"]
    }
    capitan.execute_task(tarea_asociar)

    print("\nBD de Promociones (actualizada):", PROMOCIONES_DB)
    print("-" * 20)

    # 3. Enviar campaña
    tarea_campana = {
        "type": "enviar_campana_marketing",
        "lista_clientes": ["CLI-001", "CLI-002", "CLI-003"],
        "mensaje": "¡Aprovecha nuestro 15% de descuento de verano!"
    }
    resultado_campana = capitan.execute_task(tarea_campana)
    print("Resultado Campaña:", resultado_campana)
