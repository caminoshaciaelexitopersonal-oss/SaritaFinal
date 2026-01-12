"""
Agente Capitán Táctico: CapitanReservas

Responsable de ejecutar tareas atómicas relacionadas con la creación,
cancelación y consulta de reservas de servicios turísticos.
"""

from typing import Dict, Any
import uuid
from datetime import datetime

# --- Simulación de Dependencias (Bases de Datos de otros Capitanes) ---

# Base de datos simulada de clientes (de CapitanGestionClientes)
CLIENTES_DB = {
    "CLI-123456": {"id": "CLI-123456", "nombre": "Ana García", "email": "ana.garcia@example.com"}
}

# Base de datos simulada de productos (de CapitanInventarioProductos)
PRODUCTOS_DB = {
    "PROD-ABCDE": {"id": "PROD-ABCDE", "nombre": "Tour Guiado a la Montaña", "precio": 50.0, "stock_disponible": 15}
}

# Base de datos propia de este capitán
RESERVAS_DB = {}

# --- Fin de Simulación de Dependencias ---


class CapitanReservas:
    """
    Ejecuta tareas tácticas de gestión de reservas asignadas por un Coronel.
    """

    def execute_task(self, task_payload: Dict[str, Any]) -> Dict[str, Any]:
        """
        Punto de entrada principal que enruta la tarea al método correcto.
        """
        task_type = task_payload.get("type")
        print(f"CAPITAN RESERVAS: Recibida tarea táctica '{task_type}'.")

        handler_method = getattr(self, f"_handle_{task_type}", self._handle_unknown)
        return handler_method(task_payload)

    def _handle_crear_reserva(self, task_data: Dict[str, Any]) -> Dict[str, Any]:
        """
        Lógica para crear una nueva reserva, validando cliente, producto y stock.
        """
        cliente_id = task_data.get("cliente_id")
        producto_id = task_data.get("producto_id")
        cantidad = task_data.get("cantidad", 1)

        # 1. Validar existencia de cliente y producto
        if cliente_id not in CLIENTES_DB:
            return {"status": "FAILED", "error": f"Cliente '{cliente_id}' no encontrado."}
        if producto_id not in PRODUCTOS_DB:
            return {"status": "FAILED", "error": f"Producto '{producto_id}' no encontrado."}

        # 2. Validar disponibilidad de stock
        producto = PRODUCTOS_DB[producto_id]
        if producto["stock_disponible"] < cantidad:
            return {
                "status": "FAILED",
                "error": f"Stock insuficiente para '{producto['nombre']}'. Solicitado: {cantidad}, Disponible: {producto['stock_disponible']}"
            }

        print(f"CAPITAN RESERVAS: Creando reserva de {cantidad} cupos para '{producto['nombre']}' para el cliente '{cliente_id}'.")

        # 3. Reducir el stock (simula llamada a CapitanInventarioProductos)
        PRODUCTOS_DB[producto_id]["stock_disponible"] -= cantidad
        print(f"  -> Stock de '{producto_id}' actualizado a: {PRODUCTOS_DB[producto_id]['stock_disponible']}")

        # 4. Crear la reserva
        reserva_id = f"RES-{uuid.uuid4().hex[:8].upper()}"
        RESERVAS_DB[reserva_id] = {
            "id": reserva_id,
            "cliente_id": cliente_id,
            "producto_id": producto_id,
            "cantidad": cantidad,
            "total_pagado": producto["precio"] * cantidad,
            "estado": "CONFIRMADA",
            "fecha_creacion": datetime.utcnow().isoformat()
        }

        return {
            "status": "COMPLETED",
            "result": {"reserva_id": reserva_id, "mensaje": "Reserva creada y confirmada."}
        }

    def _handle_cancelar_reserva(self, task_data: Dict[str, Any]) -> Dict[str, Any]:
        """
        Lógica para cancelar una reserva existente y restaurar el stock.
        """
        reserva_id = task_data.get("reserva_id")

        if not reserva_id or reserva_id not in RESERVAS_DB:
            return {"status": "FAILED", "error": f"Reserva con ID '{reserva_id}' no encontrada."}

        reserva = RESERVAS_DB[reserva_id]
        if reserva["estado"] == "CANCELADA":
            return {"status": "FAILED", "error": f"La reserva '{reserva_id}' ya se encuentra cancelada."}

        print(f"CAPITAN RESERVAS: Cancelando reserva '{reserva_id}'.")

        # 1. Restaurar el stock (simula llamada a CapitanInventarioProductos)
        producto_id = reserva["producto_id"]
        cantidad = reserva["cantidad"]
        if producto_id in PRODUCTOS_DB:
            PRODUCTOS_DB[producto_id]["stock_disponible"] += cantidad
            print(f"  -> Stock de '{producto_id}' restaurado a: {PRODUCTOS_DB[producto_id]['stock_disponible']}")

        # 2. Actualizar estado de la reserva
        RESERVAS_DB[reserva_id]["estado"] = "CANCELADA"

        return {"status": "COMPLETED", "result": {"reserva_id": reserva_id, "mensaje": "Reserva cancelada exitosamente."}}

    def _handle_consultar_estado_reserva(self, task_data: Dict[str, Any]) -> Dict[str, Any]:
        """Consulta el estado de una reserva por su ID."""
        reserva_id = task_data.get("reserva_id")
        if not reserva_id or reserva_id not in RESERVAS_DB:
            return {"status": "FAILED", "error": f"Reserva con ID '{reserva_id}' no encontrada."}

        return {"status": "COMPLETED", "result": {"reserva_data": RESERVAS_DB[reserva_id]}}

    def _handle_unknown(self, task_data: Dict[str, Any]) -> Dict[str, Any]:
        """Maneja tareas desconocidas."""
        return {"status": "FAILED", "error": f"El CapitanReservas no puede manejar la tarea."}

# Ejemplo de uso
if __name__ == '__main__':
    capitan = CapitanReservas()

    # 1. Crear una reserva exitosa
    print("--- Caso 1: Reserva Exitosa ---")
    tarea_crear = {"type": "crear_reserva", "cliente_id": "CLI-123456", "producto_id": "PROD-ABCDE", "cantidad": 2}
    resultado_crear = capitan.execute_task(tarea_crear)
    print("Resultado Crear:", resultado_crear)
    print("BD Reservas:", RESERVAS_DB)
    print("BD Productos:", PRODUCTOS_DB)
    print("-" * 20)

    # 2. Intentar reservar más del stock disponible
    print("\n--- Caso 2: Stock Insuficiente ---")
    tarea_stock = {"type": "crear_reserva", "cliente_id": "CLI-123456", "producto_id": "PROD-ABCDE", "cantidad": 20}
    resultado_stock = capitan.execute_task(tarea_stock)
    print("Resultado Stock:", resultado_stock)
    print("-" * 20)

    # 3. Cancelar la reserva original
    print("\n--- Caso 3: Cancelar Reserva ---")
    reserva_id = resultado_crear["result"]["reserva_id"]
    tarea_cancelar = {"type": "cancelar_reserva", "reserva_id": reserva_id}
    resultado_cancelar = capitan.execute_task(tarea_cancelar)
    print("Resultado Cancelar:", resultado_cancelar)
    print("BD Reservas:", RESERVAS_DB)
    print("BD Productos:", PRODUCTOS_DB)
    print("-" * 20)
