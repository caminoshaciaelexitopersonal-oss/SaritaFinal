"""
Agente Capitán Táctico: CapitanLogisticaYAsignacion

Responsable de ejecutar tareas atómicas relacionadas con la asignación
de recursos (guías, vehículos, equipos) a las reservas confirmadas.
"""

from typing import Dict, Any, List

# --- Simulación de Dependencias y Bases de Datos Propias ---

# Base de datos simulada de reservas (de CapitanReservas)
RESERVAS_DB = {
    "RES-1111": {"id": "RES-1111", "producto_id": "PROD-TOUR-MONTANA", "estado": "CONFIRMADA", "fecha_servicio": "2024-10-20"},
    "RES-2222": {"id": "RES-2222", "producto_id": "PROD-TOUR-CIUDAD", "estado": "CONFIRMADA", "fecha_servicio": "2024-10-20"}
}

# Base de datos propia de este capitán: Recursos disponibles
RECURSOS_DB = {
    "guias": {
        "GUIA-01": {"id": "GUIA-01", "nombre": "Carlos Mendoza", "disponible": True, "especialidad": "montañismo"},
        "GUIA-02": {"id": "GUIA-02", "nombre": "Sofia Vergara", "disponible": True, "especialidad": "historia"}
    },
    "vehiculos": {
        "VEH-JEEP-01": {"id": "VEH-JEEP-01", "placa": "WXZ456", "capacidad": 4, "tipo": "4x4", "disponible": True},
        "VEH-BUS-01": {"id": "VEH-BUS-01", "placa": "ABC123", "capacidad": 20, "tipo": "bus", "disponible": True}
    }
}

# Base de datos propia de este capitán: Asignaciones realizadas
ASIGNACIONES_DB = {} # reserva_id -> {"guia": ..., "vehiculo": ...}

# --- Fin de Simulación ---

class CapitanLogisticaYAsignacion:
    """
    Ejecuta tareas tácticas de logística y asignación de recursos.
    """

    def execute_task(self, task_payload: Dict[str, Any]) -> Dict[str, Any]:
        task_type = task_payload.get("type")
        print(f"CAPITAN LOGISTICA: Recibida tarea táctica '{task_type}'.")
        handler = getattr(self, f"_handle_{task_type}", self._handle_unknown)
        return handler(task_payload)

    def _handle_asignar_recursos_a_reserva(self, task_data: Dict[str, Any]) -> Dict[str, Any]:
        """
        Lógica completa para asignar todos los recursos necesarios a una reserva.
        """
        reserva_id = task_data.get("reserva_id")

        if reserva_id not in RESERVAS_DB:
            return {"status": "FAILED", "error": f"Reserva '{reserva_id}' no encontrada."}

        # Simulación de la lógica de negocio para elegir recursos
        guia_id = "GUIA-01" # Elegir el mejor guía según la especialidad del tour
        vehiculo_id = "VEH-JEEP-01" # Elegir el mejor vehículo según la cantidad de personas

        # Validar disponibilidad
        if not RECURSOS_DB["guias"].get(guia_id, {}).get("disponible"):
            return {"status": "FAILED", "error": f"Guía '{guia_id}' no disponible."}
        if not RECURSOS_DB["vehiculos"].get(vehiculo_id, {}).get("disponible"):
            return {"status": "FAILED", "error": f"Vehículo '{vehiculo_id}' no disponible."}

        print(f"CAPITAN LOGISTICA: Asignando Guía '{guia_id}' y Vehículo '{vehiculo_id}' a la reserva '{reserva_id}'.")

        # Marcar recursos como no disponibles
        RECURSOS_DB["guias"][guia_id]["disponible"] = False
        RECURSOS_DB["vehiculos"][vehiculo_id]["disponible"] = False

        # Guardar la asignación
        ASIGNACIONES_DB[reserva_id] = {
            "guia_id": guia_id,
            "vehiculo_id": vehiculo_id,
            "timestamp": "2024-01-01T13:00:00Z"
        }

        return {
            "status": "COMPLETED",
            "result": {"reserva_id": reserva_id, "asignaciones": ASIGNACIONES_DB[reserva_id]}
        }

    def _handle_liberar_recursos_de_reserva(self, task_data: Dict[str, Any]) -> Dict[str, Any]:
        """
        Libera los recursos asociados a una reserva (ej. por cancelación).
        """
        reserva_id = task_data.get("reserva_id")
        if reserva_id not in ASIGNACIONES_DB:
            return {"status": "FAILED", "error": f"No se encontraron asignaciones para la reserva '{reserva_id}'."}

        asignacion = ASIGNACIONES_DB[reserva_id]
        guia_id = asignacion["guia_id"]
        vehiculo_id = asignacion["vehiculo_id"]

        print(f"CAPITAN LOGISTICA: Liberando recursos de la reserva '{reserva_id}'.")

        # Marcar recursos como disponibles
        if guia_id in RECURSOS_DB["guias"]:
            RECURSOS_DB["guias"][guia_id]["disponible"] = True
        if vehiculo_id in RECURSOS_DB["vehiculos"]:
            RECURSOS_DB["vehiculos"][vehiculo_id]["disponible"] = True

        del ASIGNACIONES_DB[reserva_id]

        return {"status": "COMPLETED", "result": {"reserva_id": reserva_id, "mensaje": "Recursos liberados."}}

    def _handle_consultar_asignaciones(self, task_data: Dict[str, Any]) -> Dict[str, Any]:
        """Consulta las asignaciones para una reserva específica."""
        reserva_id = task_data.get("reserva_id")
        if reserva_id not in ASIGNACIONES_DB:
            return {"status": "FAILED", "error": f"No hay asignaciones para la reserva '{reserva_id}'."}

        return {"status": "COMPLETED", "result": {"asignaciones": ASIGNACIONES_DB[reserva_id]}}

    def _handle_unknown(self, task_data: Dict[str, Any]) -> Dict[str, Any]:
        return {"status": "FAILED", "error": f"Tarea desconocida."}

# Ejemplo de uso
if __name__ == '__main__':
    capitan = CapitanLogisticaYAsignacion()

    print("--- Caso 1: Asignación Exitosa ---")
    tarea1 = {"type": "asignar_recursos_a_reserva", "reserva_id": "RES-1111"}
    resultado1 = capitan.execute_task(tarea1)
    print("Resultado Asignación:", resultado1)
    print("BD Asignaciones:", ASIGNACIONES_DB)
    print("Disponibilidad Guía:", RECURSOS_DB["guias"]["GUIA-01"]["disponible"])
    print("-" * 20)

    print("\n--- Caso 2: Intento de Asignar a Guía Ocupado ---")
    tarea2 = {"type": "asignar_recursos_a_reserva", "reserva_id": "RES-2222"}
    resultado2 = capitan.execute_task(tarea2)
    print("Resultado Asignación Fallida:", resultado2)
    print("-" * 20)

    print("\n--- Caso 3: Liberar Recursos ---")
    tarea3 = {"type": "liberar_recursos_de_reserva", "reserva_id": "RES-1111"}
    resultado3 = capitan.execute_task(tarea3)
    print("Resultado Liberación:", resultado3)
    print("BD Asignaciones:", ASIGNACIONES_DB)
    print("Disponibilidad Guía:", RECURSOS_DB["guias"]["GUIA-01"]["disponible"])
    print("-" * 20)
