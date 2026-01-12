from typing import Dict, Any, List
from datetime import datetime

# Base de datos simulada para eventos locales
EVENTOS_LOCALES_DB: List[Dict[str, Any]] = [
    {
        "id": "evento_01",
        "nombre": "Festival de la Cachama",
        "descripcion": "Festival gastronómico y musical en Puerto Gaitán.",
        "fecha_inicio": "2024-08-15",
        "fecha_fin": "2024-08-18"
    },
    {
        "id": "evento_02",
        "nombre": "Torneo Internacional del Joropo",
        "descripcion": "Competencia de baile y música llanera en Villavicencio.",
        "fecha_inicio": "2024-06-28",
        "fecha_fin": "2024-07-01"
    }
]


class CapitanGestionDeEventosLocales:
    """
    Capitán encargado de gestionar la información sobre eventos
    culturales y turísticos a nivel municipal.
    """

    def __init__(self):
        print("CAPITÁN GESTIÓN DE EVENTOS LOCALES (MUNICIPAL): Inicializado.")
        self.eventos = EVENTOS_LOCALES_DB

    def execute_task(self, task: Dict[str, Any]) -> Dict[str, Any]:
        task_type = task.get("type")
        params = task.get("params", {})
        print(f"CAPITÁN EVENTOS: Ejecutando tarea '{task_type}' con params: {params}")

        if task_type == "consultar_eventos":
            return self._handle_consultar_eventos()
        elif task_type == "agregar_evento":
            return self._handle_agregar_evento(params)
        else:
            return {"status": "ERROR", "result": f"Tipo de tarea '{task_type}' no reconocida."}

    def _handle_consultar_eventos(self) -> Dict[str, Any]:
        return {"status": "SUCCESS", "result": self.eventos}

    def _handle_agregar_evento(self, params: Dict[str, Any]) -> Dict[str, Any]:
        nombre = params.get("nombre")
        descripcion = params.get("descripcion")
        fecha_inicio = params.get("fecha_inicio")
        fecha_fin = params.get("fecha_fin")

        if not all([nombre, descripcion, fecha_inicio, fecha_fin]):
            return {"status": "ERROR", "result": "Todos los parámetros del evento son requeridos."}

        nuevo_id = f"evento_{len(self.eventos) + 1}"
        nuevo_evento = {
            "id": nuevo_id,
            "nombre": nombre,
            "descripcion": descripcion,
            "fecha_inicio": fecha_inicio,
            "fecha_fin": fecha_fin
        }
        self.eventos.append(nuevo_evento)
        print(f"CAPITÁN EVENTOS: Nuevo evento '{nombre}' agregado con ID '{nuevo_id}'.")
        return {"status": "SUCCESS", "result": nuevo_evento}
