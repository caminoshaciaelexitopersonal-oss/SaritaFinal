"""
Agente Capitán Táctico: CapitanVentas

Responsable de ejecutar tareas atómicas relacionadas con el ciclo de ventas.
"""

from typing import Dict, Any
import uuid

class CapitanVentas:
    """
    Ejecuta tareas tácticas de ventas asignadas por un Coronel.
    """

    def execute_task(self, task_payload: Dict[str, Any]) -> Dict[str, Any]:
        """
        Punto de entrada principal que enruta la tarea al método correcto.
        """
        task_type = task_payload.get("type")
        print(f"CAPITAN VENTAS: Recibida tarea táctica '{task_type}'.")

        handler_method = getattr(self, f"_handle_{task_type}", self._handle_unknown)
        return handler_method(task_payload)

    def _handle_crear_factura(self, task_data: Dict[str, Any]) -> Dict[str, Any]:
        """
        Lógica para crear una nueva factura.

        En un sistema real, esto interactuaría con el servicio de facturación
        o directamente con el modelo de Django a través de una capa de servicio.
        """
        print(f"CAPITAN VENTAS: Procesando creación de factura para cliente '{task_data.get('cliente_id')}'.")

        # Simulación de la creación de la factura
        factura_id = f"FV-{uuid.uuid4().hex[:8].upper()}"
        total = sum(item.get('precio', 0) * item.get('cantidad', 0) for item in task_data.get('items', []))

        print(f"CAPITAN VENTAS: Factura '{factura_id}' creada con un total de ${total:.2f}.")

        return {
            "status": "COMPLETED",
            "result": {
                "factura_id": factura_id,
                "total": total,
                "mensaje": "Factura creada exitosamente en el sistema."
            }
        }

    def _handle_enviar_factura_email(self, task_data: Dict[str, Any]) -> Dict[str, Any]:
        """
        Lógica para enviar una factura por correo electrónico.
        """
        factura_id = task_data.get("factura_id")
        email_cliente = task_data.get("email", "no_proporcionado")

        print(f"CAPITAN VENTAS: Enviando factura '{factura_id}' al email '{email_cliente}'.")

        # Simulación del envío de correo
        print("CAPITAN VENTAS: Conectando con servicio de email y enviando...")

        return {
            "status": "COMPLETED",
            "result": {
                "factura_id": factura_id,
                "notificacion_enviada": True,
                "mensaje": f"Factura {factura_id} enviada correctamente a {email_cliente}."
            }
        }

    def _handle_unknown(self, task_data: Dict[str, Any]) -> Dict[str, Any]:
        """Maneja tareas desconocidas para este capitán."""
        task_type = task_data.get("type")
        print(f"CAPITAN VENTAS: Error - Tarea táctica desconocida: '{task_type}'.")
        return {
            "status": "FAILED",
            "error": f"El CapitanVentas no puede manejar la tarea de tipo '{task_type}'."
        }
