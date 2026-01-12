import uuid
from typing import Dict, Any, List
from datetime import datetime

# Base de datos simulada en memoria para los tickets de PQRS
PQRS_DB: List[Dict[str, Any]] = []


class CapitanPQRS:
    """
    Capitán encargado de la gestión de Peticiones, Quejas, Reclamos y Sugerencias.
    """

    def __init__(self):
        print("CAPITÁN PQRS: Inicializado.")
        self.pqrs_tickets = PQRS_DB

    def execute_task(self, task: Dict[str, Any]) -> Dict[str, Any]:
        task_type = task.get("type")
        params = task.get("params", {})
        print(f"CAPITÁN PQRS: Ejecutando tarea '{task_type}' con params: {params}")

        if task_type == "radicar_pqr":
            return self._handle_radicar_pqr(params)
        elif task_type == "consultar_pqr":
            return self._handle_consultar_pqr(params)
        else:
            return {"status": "ERROR", "result": f"Tipo de tarea '{task_type}' no reconocida."}

    def _handle_radicar_pqr(self, params: Dict[str, Any]) -> Dict[str, Any]:
        user_id = params.get("user_id")
        tipo_solicitud = params.get("tipo_solicitud")  # Peticion, Queja, Reclamo, Sugerencia
        mensaje = params.get("mensaje")

        if not all([user_id, tipo_solicitud, mensaje]):
            return {"status": "ERROR", "result": "Los parámetros 'user_id', 'tipo_solicitud' y 'mensaje' son requeridos."}

        ticket_id = f"pqr_{uuid.uuid4().hex[:10]}"
        nuevo_ticket = {
            "id": ticket_id,
            "user_id": user_id,
            "tipo_solicitud": tipo_solicitud,
            "mensaje": mensaje,
            "estado": "RECIBIDO",
            "fecha_creacion": datetime.utcnow().isoformat()
        }
        self.pqrs_tickets.append(nuevo_ticket)

        print(f"CAPITÁN PQRS: Nuevo ticket radicado con ID: {ticket_id}")
        return {"status": "SUCCESS", "result": nuevo_ticket}

    def _handle_consultar_pqr(self, params: Dict[str, Any]) -> Dict[str, Any]:
        ticket_id = params.get("id")
        if not ticket_id:
            return {"status": "ERROR", "result": "El parámetro 'id' es requerido."}

        resultado = next((t for t in self.pqrs_tickets if t.get("id") == ticket_id), None)
        if resultado:
            return {"status": "SUCCESS", "result": resultado}
        else:
            return {"status": "NOT_FOUND", "result": f"Ticket PQR con id '{ticket_id}' no encontrado."}
