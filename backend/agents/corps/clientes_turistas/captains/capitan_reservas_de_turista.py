import uuid
from typing import Dict, Any, List

# Se importa la BD de servicios para simular la verificación de disponibilidad
from .capitan_busqueda_de_servicios import SERVICIOS_DB

# Base de datos simulada en memoria para las reservas
RESERVAS_DB: List[Dict[str, Any]] = []


class CapitanReservasDeTurista:
    """
    Capitán encargado de gestionar las reservas de servicios para los turistas.
    """

    def __init__(self):
        print("CAPITÁN RESERVAS DE TURISTA: Inicializado.")
        self.reservas = RESERVAS_DB
        self.servicios = SERVICIOS_DB

    def execute_task(self, task: Dict[str, Any]) -> Dict[str, Any]:
        task_type = task.get("type")
        params = task.get("params", {})
        print(f"CAPITÁN RESERVAS: Ejecutando tarea '{task_type}' con params: {params}")

        if task_type == "crear_reserva":
            return self._handle_crear_reserva(params)
        elif task_type == "consultar_reserva":
            return self._handle_consultar_reserva(params)
        else:
            return {"status": "ERROR", "result": f"Tipo de tarea '{task_type}' no reconocida."}

    def _handle_crear_reserva(self, params: Dict[str, Any]) -> Dict[str, Any]:
        servicio_id = params.get("servicio_id")
        user_id = params.get("user_id")
        fecha = params.get("fecha")

        if not all([servicio_id, user_id, fecha]):
            return {"status": "ERROR", "result": "Los parámetros 'servicio_id', 'user_id' y 'fecha' son requeridos."}

        # Verificar si el servicio existe y está disponible
        servicio = next((s for s in self.servicios if s.get("id") == servicio_id), None)
        if not servicio:
            return {"status": "NOT_FOUND", "result": f"Servicio con id '{servicio_id}' no encontrado."}

        if not servicio.get("disponibilidad", False):
            return {"status": "UNAVAILABLE", "result": f"El servicio '{servicio.get('nombre')}' no está disponible."}

        # Crear la reserva
        reserva_id = f"res_{uuid.uuid4().hex[:8]}"
        nueva_reserva = {
            "id": reserva_id,
            "servicio_id": servicio_id,
            "nombre_servicio": servicio.get("nombre"),
            "user_id": user_id,
            "fecha_reserva": fecha,
            "estado": "CONFIRMADA"
        }
        self.reservas.append(nueva_reserva)

        print(f"CAPITÁN RESERVAS: Nueva reserva creada con ID: {reserva_id}")
        return {"status": "SUCCESS", "result": nueva_reserva}

    def _handle_consultar_reserva(self, params: Dict[str, Any]) -> Dict[str, Any]:
        reserva_id = params.get("id")
        if not reserva_id:
            return {"status": "ERROR", "result": "El parámetro 'id' es requerido."}

        resultado = next((r for r in self.reservas if r.get("id") == reserva_id), None)
        if resultado:
            return {"status": "SUCCESS", "result": resultado}
        else:
            return {"status": "NOT_FOUND", "result": f"Reserva con id '{reserva_id}' no encontrada."}
