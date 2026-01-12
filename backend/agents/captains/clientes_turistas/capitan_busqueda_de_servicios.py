"""
Agente Capitán Táctico: CapitanBusquedaDeServicios

Responsable de buscar y filtrar la oferta turística disponible
(destinos, servicios, etc.) según los criterios del usuario.
"""

from typing import Dict, Any, List

# --- Simulación de la Base de Datos de Oferta Turística ---
OFERTA_TURISTICA_DB = {
    "DEST-01": {"id": "DEST-01", "nombre": "Cañón del Chicamocha", "tipo": "destino", "tags": ["naturaleza", "aventura"]},
    "DEST-02": {"id": "DEST-02", "nombre": "Villa de Leyva", "tipo": "destino", "tags": ["historia", "pueblo"]},
    "SERV-01": {
        "id": "SERV-01", "nombre": "Parapente en el Cañón", "destino_id": "DEST-01", "tipo": "servicio",
        "tags": ["extremo", "aventura"], "precio_por_persona": 180.00, "disponibilidad": ["2024-11-10", "2024-11-12", "2024-11-15"]
    },
    "SERV-02": {
        "id": "SERV-02", "nombre": "Tour Histórico a Pie", "destino_id": "DEST-02", "tipo": "servicio",
        "tags": ["cultural", "historia"], "precio_por_persona": 45.00, "disponibilidad": ["2024-11-10", "2024-11-11"]
    }
}
# --- Fin de Simulación ---

class CapitanBusquedaDeServicios:
    """
    Ejecuta tareas tácticas de búsqueda sobre la oferta turística.
    """

    def execute_task(self, task_payload: Dict[str, Any]) -> Dict[str, Any]:
        task_type = task_payload.get("type")
        print(f"CAPITAN BUSQUEDA TURISTAS: Recibida tarea táctica '{task_type}'.")
        handler = getattr(self, f"_handle_{task_type}", self._handle_unknown)
        return handler(task_payload)

    def _handle_buscar_por_tags(self, task_data: Dict[str, Any]) -> Dict[str, Any]:
        """
        Busca destinos o servicios que coincidan con una lista de tags.
        """
        tags_busqueda = set(task_data.get("tags", []))
        if not tags_busqueda:
            return {"status": "FAILED", "error": "Se requiere al menos un tag para la búsqueda."}

        print(f"CAPITAN BUSQUEDA TURISTAS: Buscando por tags: {tags_busqueda}")

        resultados = []
        for item_id, item_data in OFERTA_TURISTICA_DB.items():
            item_tags = set(item_data.get("tags", []))
            if tags_busqueda.intersection(item_tags):
                resultados.append(item_data)

        return {"status": "COMPLETED", "result": {"resultados": resultados}}

    def _handle_buscar_servicios_por_fecha(self, task_data: Dict[str, Any]) -> Dict[str, Any]:
        """
        Busca servicios disponibles en una fecha específica.
        """
        fecha = task_data.get("fecha")
        if not fecha:
            return {"status": "FAILED", "error": "Se requiere una fecha para la búsqueda."}

        print(f"CAPITAN BUSQUEDA TURISTAS: Buscando servicios disponibles para la fecha: {fecha}")

        resultados = []
        for item_id, item_data in OFERTA_TURISTICA_DB.items():
            if item_data.get("tipo") == "servicio" and fecha in item_data.get("disponibilidad", []):
                resultados.append(item_data)

        return {"status": "COMPLETED", "result": {"resultados": resultados}}

    def _handle_unknown(self, task_data: Dict[str, Any]) -> Dict[str, Any]:
        return {"status": "FAILED", "error": "Tipo de búsqueda no soportado."}

# Ejemplo de uso
if __name__ == '__main__':
    capitan = CapitanBusquedaDeServicios()

    print("--- Caso 1: Búsqueda por tag 'aventura' ---")
    tarea1 = {"type": "buscar_por_tags", "tags": ["aventura"]}
    resultado1 = capitan.execute_task(tarea1)
    print("Resultados:", [item['nombre'] for item in resultado1['result']['resultados']])
    print("-" * 20)

    print("\n--- Caso 2: Búsqueda por fecha '2024-11-10' ---")
    tarea2 = {"type": "buscar_servicios_por_fecha", "fecha": "2024-11-10"}
    resultado2 = capitan.execute_task(tarea2)
    print("Resultados:", [item['nombre'] for item in resultado2['result']['resultados']])
    print("-" * 20)
