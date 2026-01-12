from typing import Dict, Any, List

# Se importa la BD de reservas para simular la consulta del historial
from .capitan_reservas_de_turista import RESERVAS_DB

# Base de datos simulada en memoria para perfiles de usuario
PERFILES_DB: Dict[str, Dict[str, Any]] = {
    "user_001": {
        "id": "user_001",
        "nombre": "Juan Turista",
        "email": "juan.turista@example.com",
        "preferencias": ["naturaleza", "aventura"]
    },
    "user_002": {
        "id": "user_002",
        "nombre": "Ana Viajera",
        "email": "ana.viajera@example.com",
        "preferencias": ["cultura", "gastronomía"]
    }
}


class CapitanGestionDePerfil:
    """
    Capitán encargado de la gestión del perfil de los turistas.
    """

    def __init__(self):
        print("CAPITÁN GESTIÓN DE PERFIL: Inicializado.")
        self.perfiles = PERFILES_DB
        self.reservas = RESERVAS_DB

    def execute_task(self, task: Dict[str, Any]) -> Dict[str, Any]:
        task_type = task.get("type")
        params = task.get("params", {})
        print(f"CAPITÁN PERFIL: Ejecutando tarea '{task_type}' con params: {params}")

        if task_type == "ver_perfil":
            return self._handle_ver_perfil(params)
        elif task_type == "actualizar_preferencias":
            return self._handle_actualizar_preferencias(params)
        elif task_type == "ver_historial_reservas":
            return self._handle_ver_historial_reservas(params)
        else:
            return {"status": "ERROR", "result": f"Tipo de tarea '{task_type}' no reconocida."}

    def _handle_ver_perfil(self, params: Dict[str, Any]) -> Dict[str, Any]:
        user_id = params.get("user_id")
        if not user_id:
            return {"status": "ERROR", "result": "El parámetro 'user_id' es requerido."}

        perfil = self.perfiles.get(user_id)
        if perfil:
            return {"status": "SUCCESS", "result": perfil}
        else:
            return {"status": "NOT_FOUND", "result": f"Perfil con user_id '{user_id}' no encontrado."}

    def _handle_actualizar_preferencias(self, params: Dict[str, Any]) -> Dict[str, Any]:
        user_id = params.get("user_id")
        nuevas_preferencias = params.get("preferencias")

        if not user_id or nuevas_preferencias is None:
            return {"status": "ERROR", "result": "Los parámetros 'user_id' y 'preferencias' son requeridos."}

        perfil = self.perfiles.get(user_id)
        if not perfil:
            return {"status": "NOT_FOUND", "result": f"Perfil con user_id '{user_id}' no encontrado."}

        perfil["preferencias"] = nuevas_preferencias
        print(f"CAPITÁN PERFIL: Preferencias actualizadas para el usuario {user_id}.")
        return {"status": "SUCCESS", "result": perfil}

    def _handle_ver_historial_reservas(self, params: Dict[str, Any]) -> Dict[str, Any]:
        user_id = params.get("user_id")
        if not user_id:
            return {"status": "ERROR", "result": "El parámetro 'user_id' es requerido."}

        historial = [r for r in self.reservas if r.get("user_id") == user_id]
        return {"status": "SUCCESS", "result": historial}
