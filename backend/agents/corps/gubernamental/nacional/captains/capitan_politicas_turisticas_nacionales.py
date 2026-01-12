from typing import Dict, Any, List

# Base de datos simulada para políticas turísticas nacionales
POLITICAS_NACIONALES_DB: Dict[str, Dict[str, Any]] = {
    "POL_001": {
        "nombre": "Certificación de Sostenibilidad Turística",
        "descripcion": "Sello de calidad para prestadores que cumplen con estándares ambientales y socioculturales.",
        "activa": True
    },
    "POL_002": {
        "nombre": "Fomento al Turismo en Zonas de Posconflicto",
        "descripcion": "Incentivos fiscales para la inversión turística en regiones específicas.",
        "activa": True
    }
}


class CapitanPoliticasTuristicasNacionales:
    """
    Capitán encargado de la gestión de políticas y estándares
    turísticos a nivel nacional.
    """

    def __init__(self):
        print("CAPITÁN POLÍTICAS TURÍSTICAS (NACIONAL): Inicializado.")
        self.politicas = POLITICAS_NACIONALES_DB

    def execute_task(self, task: Dict[str, Any]) -> Dict[str, Any]:
        task_type = task.get("type")
        params = task.get("params", {})
        print(f"CAPITÁN POLÍTICAS: Ejecutando tarea '{task_type}' con params: {params}")

        if task_type == "consultar_politicas_activas":
            return self._handle_consultar_politicas_activas()
        elif task_type == "proponer_nueva_politica":
            return self._handle_proponer_nueva_politica(params)
        else:
            return {"status": "ERROR", "result": f"Tipo de tarea '{task_type}' no reconocida."}

    def _handle_consultar_politicas_activas(self) -> Dict[str, Any]:
        politicas_activas = {k: v for k, v in self.politicas.items() if v.get("activa")}
        return {"status": "SUCCESS", "result": politicas_activas}

    def _handle_proponer_nueva_politica(self, params: Dict[str, Any]) -> Dict[str, Any]:
        nombre = params.get("nombre")
        descripcion = params.get("descripcion")

        if not all([nombre, descripcion]):
            return {"status": "ERROR", "result": "Los parámetros 'nombre' y 'descripcion' son requeridos."}

        nuevo_id = f"POL_{len(self.politicas) + 1:03d}"
        nueva_politica = {
            "nombre": nombre,
            "descripcion": descripcion,
            "activa": False  # Las nuevas políticas inician como propuestas (inactivas)
        }
        self.politicas[nuevo_id] = nueva_politica
        print(f"CAPITÁN POLÍTICAS: Nueva política '{nombre}' propuesta con ID '{nuevo_id}'.")
        return {"status": "SUCCESS", "result": nueva_politica}
