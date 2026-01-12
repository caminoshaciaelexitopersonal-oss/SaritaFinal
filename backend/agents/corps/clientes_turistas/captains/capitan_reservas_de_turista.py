"""
Agente Capitán Táctico: CapitanReservasDeTurista

Responsable de gestionar el ciclo de vida de las reservas desde la
perspectiva del turista (iniciar, cancelar, consultar).
"""

from typing import Dict, Any
import uuid
from datetime import datetime

# --- Simulación de Dependencias y Bases de Datos Propias ---

# Base de datos de oferta turística (de CapitanBusquedaDeServicios)
OFERTA_TURISTICA_DB = {
    "SERV-01": {
        "id": "SERV-01", "nombre": "Parapente en el Cañón", "precio_por_persona": 180.00,
        "disponibilidad": {"2024-11-15": 10, "2024-11-16": 5}
    }
}

# Base de datos propia de este capitán
RESERVAS_TURISTA_DB = {}

# --- Fin de Simulación ---

class CapitanReservasDeTurista:
    """
    Ejecuta tareas tácticas de gestión de reservas para turistas.
    """

    def execute_task(self, task_payload: Dict[str, Any]) -> Dict[str, Any]:
        task_type = task_payload.get("type")
        print(f"CAPITAN RESERVAS (TURISTA): Recibida tarea táctica '{task_type}'.")
        handler = getattr(self, f"_handle_{task_type}", self._handle_unknown)
        return handler(task_payload)

    def _handle_iniciar_reserva_servicio(self, task_data: Dict[str, Any]) -> Dict[str, Any]:
        """
        Inicia una reserva para un servicio, validando disponibilidad y cupos.
        """
        turista_id = task_data.get("turista_id")
        servicio_id = task_data.get("servicio_id")
        fecha = task_data.get("fecha")
        cantidad_personas = task_data.get("cantidad_personas", 1)

        # 1. Validar que el servicio existe
        if servicio_id not in OFERTA_TURISTICA_DB:
            return {"status": "FAILED", "error": f"Servicio '{servicio_id}' no encontrado."}

        servicio = OFERTA_TURISTICA_DB[servicio_id]

        # 2. Validar disponibilidad y cupos
        cupos_disponibles = servicio.get("disponibilidad", {}).get(fecha, 0)
        if cupos_disponibles < cantidad_personas:
            return {"status": "FAILED", "error": f"No hay cupos suficientes para '{servicio['nombre']}' en la fecha {fecha}. Disponibles: {cupos_disponibles}"}

        print(f"CAPITAN RESERVAS (TURISTA): Iniciando reserva para {cantidad_personas} personas en '{servicio['nombre']}'.")

        # 3. Crear la reserva en estado 'PENDIENTE'
        reserva_id = f"RES-TUR-{uuid.uuid4().hex[:6].upper()}"
        RESERVAS_TURISTA_DB[reserva_id] = {
            "id": reserva_id, "turista_id": turista_id, "servicio_id": servicio_id,
            "fecha": fecha, "cantidad_personas": cantidad_personas,
            "estado": "PENDIENTE_PAGO", "timestamp": datetime.utcnow().isoformat()
        }

        # En un sistema real, el siguiente paso sería orquestar una llamada
        # al Capitán de Cuentas por Cobrar para generar el enlace de pago.

        return {"status": "COMPLETED", "result": {"reserva_id": reserva_id, "estado": "PENDIENTE_PAGO"}}

    def _handle_cancelar_reserva_turista(self, task_data: Dict[str, Any]) -> Dict[str, Any]:
        """
        Cancela una reserva iniciada por un turista.
        """
        reserva_id = task_data.get("reserva_id")

        if reserva_id not in RESERVAS_TURISTA_DB:
            return {"status": "FAILED", "error": f"Reserva '{reserva_id}' no encontrada."}

        reserva = RESERVAS_TURISTA_DB[reserva_id]
        if reserva["estado"] == "CANCELADA":
            return {"status": "FAILED", "error": "La reserva ya está cancelada."}

        print(f"CAPITAN RESERVAS (TURISTA): Cancelando reserva '{reserva_id}'.")
        reserva["estado"] = "CANCELADA"

        # En un sistema real, esto orquestaría una llamada para restaurar cupos si ya
        # se habían descontado y procesar un reembolso si correspondía.

        return {"status": "COMPLETED", "result": {"reserva_id": reserva_id, "estado": "CANCELADA"}}

    def _handle_unknown(self, task_data: Dict[str, Any]) -> Dict[str, Any]:
        return {"status": "FAILED", "error": "Tarea de reserva de turista desconocida."}

# Ejemplo de uso
if __name__ == '__main__':
    capitan = CapitanReservasDeTurista()

    print("--- Caso 1: Iniciar una reserva con cupos disponibles ---")
    tarea1 = {
        "type": "iniciar_reserva_servicio", "turista_id": "TUR-777",
        "servicio_id": "SERV-01", "fecha": "2024-11-15", "cantidad_personas": 4
    }
    resultado1 = capitan.execute_task(tarea1)
    print("Resultado:", resultado1)
    print("BD Reservas Turista:", RESERVAS_TURISTA_DB)
    print("-" * 20)

    print("\n--- Caso 2: Intentar reservar sin cupos suficientes ---")
    tarea2 = {
        "type": "iniciar_reserva_servicio", "turista_id": "TUR-888",
        "servicio_id": "SERV-01", "fecha": "2024-11-16", "cantidad_personas": 10
    }
    resultado2 = capitan.execute_task(tarea2)
    print("Resultado:", resultado2)
    print("-" * 20)

    print("\n--- Caso 3: Cancelar la primera reserva ---")
    reserva_a_cancelar = resultado1["result"]["reserva_id"]
    tarea3 = {"type": "cancelar_reserva_turista", "reserva_id": reserva_a_cancelar}
    resultado3 = capitan.execute_task(tarea3)
    print("Resultado:", resultado3)
    print("BD Reservas Turista (actualizada):", RESERVAS_TURISTA_DB)
    print("-" * 20)
