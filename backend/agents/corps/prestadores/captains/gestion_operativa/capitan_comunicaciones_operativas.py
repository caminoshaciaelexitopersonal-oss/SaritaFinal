"""
Agente Capitán Táctico: CapitanComunicacionesOperativas

Responsable de ejecutar tareas atómicas de comunicación transaccional
con los clientes (confirmaciones, recordatorios, etc.).
"""

from typing import Dict, Any

# --- Simulación de Dependencias (Bases de Datos de otros Capitanes) ---

CLIENTES_DB = {
    "CLI-123": {"id": "CLI-123", "nombre": "Elena Petrova", "email": "elena.p@example.com"},
}

RESERVAS_DB = {
    "RES-XYZ-789": {"id": "RES-XYZ-789", "cliente_id": "CLI-123", "producto_nombre": "Excursión al Volcán", "fecha_servicio": "2024-11-15"}
}

# --- Fin de Simulación ---

class CapitanComunicacionesOperativas:
    """
    Ejecuta tareas tácticas de comunicación operativa con clientes.
    """

    def execute_task(self, task_payload: Dict[str, Any]) -> Dict[str, Any]:
        task_type = task_payload.get("type")
        print(f"CAPITAN COMUNICACIONES: Recibida tarea táctica '{task_type}'.")
        handler = getattr(self, f"_handle_{task_type}", self._handle_unknown)
        return handler(task_payload)

    def _handle_enviar_confirmacion_reserva(self, task_data: Dict[str, Any]) -> Dict[str, Any]:
        """
        Envía un email de confirmación de reserva al cliente.
        """
        reserva_id = task_data.get("reserva_id")

        if reserva_id not in RESERVAS_DB:
            return {"status": "FAILED", "error": f"Reserva '{reserva_id}' no encontrada."}

        reserva = RESERVAS_DB[reserva_id]
        cliente = CLIENTES_DB.get(reserva["cliente_id"])

        if not cliente:
            return {"status": "FAILED", "error": f"Cliente para la reserva '{reserva_id}' no encontrado."}

        asunto = f"Confirmación de tu reserva #{reserva_id}"
        cuerpo = f"Hola {cliente['nombre']},\n\nTu reserva para '{reserva['producto_nombre']}' el {reserva['fecha_servicio']} ha sido confirmada.\n\n¡Gracias por elegirnos!"

        return self._simular_envio_email(cliente['email'], asunto, cuerpo)

    def _handle_enviar_recordatorio_viaje(self, task_data: Dict[str, Any]) -> Dict[str, Any]:
        """
        Envía un recordatorio de un próximo servicio.
        """
        reserva_id = task_data.get("reserva_id")
        dias_antes = task_data.get("dias_antes", 3)

        if reserva_id not in RESERVAS_DB:
            return {"status": "FAILED", "error": f"Reserva '{reserva_id}' no encontrada."}

        reserva = RESERVAS_DB[reserva_id]
        cliente = CLIENTES_DB.get(reserva["cliente_id"])

        if not cliente:
            return {"status": "FAILED", "error": f"Cliente para la reserva '{reserva_id}' no encontrado."}

        asunto = f"Recordatorio de tu próxima aventura: {reserva['producto_nombre']}"
        cuerpo = f"Hola {cliente['nombre']},\n\nSolo un recordatorio de que tu servicio '{reserva['producto_nombre']}' está programado para el {reserva['fecha_servicio']}.\n\n¡Te esperamos!"

        return self._simular_envio_email(cliente['email'], asunto, cuerpo)

    def _handle_solicitar_feedback_post_servicio(self, task_data: Dict[str, Any]) -> Dict[str, Any]:
        """
        Envía un email solicitando feedback después de completado el servicio.
        """
        reserva_id = task_data.get("reserva_id")
        if reserva_id not in RESERVAS_DB:
            return {"status": "FAILED", "error": f"Reserva '{reserva_id}' no encontrada."}

        reserva = RESERVAS_DB[reserva_id]
        cliente = CLIENTES_DB.get(reserva["cliente_id"])

        asunto = f"¿Cómo fue tu experiencia en '{reserva['producto_nombre']}'?"
        cuerpo = f"Hola {cliente['nombre']},\n\nEsperamos que hayas disfrutado tu servicio. ¿Podrías dedicarnos un momento para dejarnos tu opinión? Tu feedback es muy valioso."

        return self._simular_envio_email(cliente['email'], asunto, cuerpo)

    def _simular_envio_email(self, destinatario: str, asunto: str, cuerpo: str) -> Dict[str, Any]:
        """Simula la interacción con un servicio de envío de correos."""
        print(f"CAPITAN COMUNICACIONES: Simulando envío de email a '{destinatario}'.")
        print(f"  Asunto: {asunto}")
        # print(f"  Cuerpo: {cuerpo}")

        # Simulación de una operación que puede fallar
        if "fail" in destinatario:
            return {"status": "FAILED", "error": "Servicio de email no disponible."}

        return {
            "status": "COMPLETED",
            "result": {"destinatario": destinatario, "asunto": asunto, "mensaje": "Comunicación enviada exitosamente."}
        }

    def _handle_unknown(self, task_data: Dict[str, Any]) -> Dict[str, Any]:
        return {"status": "FAILED", "error": "Tipo de comunicación no soportada."}

# Ejemplo de uso
if __name__ == '__main__':
    capitan = CapitanComunicacionesOperativas()

    print("--- Caso 1: Enviar Confirmación ---")
    tarea1 = {"type": "enviar_confirmacion_reserva", "reserva_id": "RES-XYZ-789"}
    resultado1 = capitan.execute_task(tarea1)
    print("Resultado:", resultado1)
    print("-" * 20)

    print("\n--- Caso 2: Enviar Recordatorio ---")
    tarea2 = {"type": "enviar_recordatorio_viaje", "reserva_id": "RES-XYZ-789"}
    resultado2 = capitan.execute_task(tarea2)
    print("Resultado:", resultado2)
    print("-" * 20)

    print("\n--- Caso 3: Solicitar Feedback ---")
    tarea3 = {"type": "solicitar_feedback_post_servicio", "reserva_id": "RES-XYZ-789"}
    resultado3 = capitan.execute_task(tarea3)
    print("Resultado:", resultado3)
    print("-" * 20)
