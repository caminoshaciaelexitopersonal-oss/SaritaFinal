from typing import Dict, Any, List

# Base de datos simulada para rutas turísticas departamentales
RUTAS_DEPARTAMENTALES_DB: List[Dict[str, Any]] = [
    {
        "id": "ruta_01",
        "nombre": "Ruta del Amanecer Llanero",
        "descripcion": "Un recorrido por los municipios de Villavicencio, Acacías y San Martín, observando los paisajes llaneros.",
        "municipios": ["Villavicencio", "Acacías", "San Martín"],
        "duracion_dias": 3
    },
    {
        "id": "ruta_02",
        "nombre": "Ruta del Embrujo Llanero",
        "descripcion": "Explora la magia de los ríos y la cultura en Puerto López y Puerto Gaitán.",
        "municipios": ["Puerto López", "Puerto Gaitán"],
        "duracion_dias": 4
    }
]


class CapitanGestionDeRutasTuristicas:
    """
    Capitán encargado de la gestión de rutas turísticas a nivel departamental.
    """

    def __init__(self):
        print("CAPITÁN GESTIÓN DE RUTAS TURÍSTICAS (DEPARTAMENTAL): Inicializado.")
        self.rutas = RUTAS_DEPARTAMENTALES_DB

    def execute_task(self, task: Dict[str, Any]) -> Dict[str, Any]:
        task_type = task.get("type")
        params = task.get("params", {})
        print(f"CAPITÁN RUTAS: Ejecutando tarea '{task_type}' con params: {params}")

        if task_type == "consultar_rutas":
            return self._handle_consultar_rutas()
        elif task_type == "crear_ruta":
            return self._handle_crear_ruta(params)
        else:
            return {"status": "ERROR", "result": f"Tipo de tarea '{task_type}' no reconocida."}

    def _handle_consultar_rutas(self) -> Dict[str, Any]:
        return {"status": "SUCCESS", "result": self.rutas}

    def _handle_crear_ruta(self, params: Dict[str, Any]) -> Dict[str, Any]:
        nombre = params.get("nombre")
        descripcion = params.get("descripcion")
        municipios = params.get("municipios")
        duracion_dias = params.get("duracion_dias")

        if not all([nombre, descripcion, municipios, duracion_dias]):
            return {"status": "ERROR", "result": "Todos los parámetros de la ruta son requeridos."}

        nuevo_id = f"ruta_{len(self.rutas) + 1}"
        nueva_ruta = {
            "id": nuevo_id,
            "nombre": nombre,
            "descripcion": descripcion,
            "municipios": municipios,
            "duracion_dias": duracion_dias
        }
        self.rutas.append(nueva_ruta)
        print(f"CAPITÁN RUTAS: Nueva ruta '{nombre}' creada con ID '{nuevo_id}'.")
        return {"status": "SUCCESS", "result": nueva_ruta}
