from typing import Dict, Any, List

# Base de datos simulada en memoria para servicios turísticos
SERVICIOS_DB: List[Dict[str, Any]] = [
    {
        "id": "hotel_001",
        "tipo": "hotel",
        "nombre": "Hotel El Mirador del Llano",
        "destino": "Villavicencio",
        "descripcion": "Disfruta de una vista espectacular y una piscina increíble.",
        "precio_por_noche": 250000,
        "disponibilidad": True
    },
    {
        "id": "tour_001",
        "tipo": "tour",
        "nombre": "Safari por los Llanos",
        "destino": "Puerto López",
        "descripcion": "Una aventura para observar la fauna silvestre: chigüiros, venados y aves.",
        "precio_por_persona": 180000,
        "duracion_horas": 6
    },
    {
        "id": "rest_001",
        "tipo": "restaurante",
        "nombre": "La Mamona del Abuelo",
        "destino": "Villavicencio",
        "descripcion": "La mejor carne a la llanera de la región.",
        "rango_precios": "30,000 - 80,000 COP"
    },
    {
        "id": "hotel_002",
        "tipo": "hotel",
        "nombre": "Finca Hotel La Vorágine",
        "destino": "Puerto López",
        "descripcion": "Alojamiento rural con todas las comodidades modernas.",
        "precio_por_noche": 190000,
        "disponibilidad": False
    },
]


class CapitanBusquedaDeServicios:
    """
    Capitán encargado de la búsqueda y consulta de servicios turísticos.
    """

    def __init__(self):
        print("CAPITÁN BÚSQUEDA DE SERVICIOS: Inicializado.")
        self.servicios = SERVICIOS_DB

    def execute_task(self, task: Dict[str, Any]) -> Dict[str, Any]:
        task_type = task.get("type")
        params = task.get("params", {})
        print(f"CAPITÁN BÚSQUEDA: Ejecutando tarea '{task_type}' con params: {params}")

        if task_type == "buscar_por_destino":
            return self._handle_buscar_por_destino(params)
        elif task_type == "buscar_por_tipo":
            return self._handle_buscar_por_tipo(params)
        elif task_type == "ver_detalle":
            return self._handle_ver_detalle(params)
        else:
            return {"status": "ERROR", "result": f"Tipo de tarea '{task_type}' no reconocida."}

    def _handle_buscar_por_destino(self, params: Dict[str, Any]) -> Dict[str, Any]:
        destino = params.get("destino")
        if not destino:
            return {"status": "ERROR", "result": "El parámetro 'destino' es requerido."}

        resultados = [s for s in self.servicios if s.get("destino", "").lower() == destino.lower()]
        return {"status": "SUCCESS", "result": resultados}

    def _handle_buscar_por_tipo(self, params: Dict[str, Any]) -> Dict[str, Any]:
        tipo = params.get("tipo")
        if not tipo:
            return {"status": "ERROR", "result": "El parámetro 'tipo' es requerido."}

        resultados = [s for s in self.servicios if s.get("tipo", "").lower() == tipo.lower()]
        return {"status": "SUCCESS", "result": resultados}

    def _handle_ver_detalle(self, params: Dict[str, Any]) -> Dict[str, Any]:
        servicio_id = params.get("id")
        if not servicio_id:
            return {"status": "ERROR", "result": "El parámetro 'id' es requerido."}

        resultado = next((s for s in self.servicios if s.get("id") == servicio_id), None)
        if resultado:
            return {"status": "SUCCESS", "result": resultado}
        else:
            return {"status": "NOT_FOUND", "result": f"Servicio con id '{servicio_id}' no encontrado."}
