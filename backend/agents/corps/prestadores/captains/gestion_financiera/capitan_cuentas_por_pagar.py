"""
Agente Capitán Táctico: CapitanCuentasPorPagar

Responsable de gestionar las facturas de proveedores y programar sus pagos.
"""

from typing import Dict, Any, List
from decimal import Decimal
import uuid
from datetime import datetime, date

# Base de datos simulada de cuentas por pagar
CUENTAS_POR_PAGAR_DB = {}

class CapitanCuentasPorPagar:
    """
    Ejecuta tareas tácticas de gestión de cuentas por pagar.
    """

    def execute_task(self, task_payload: Dict[str, Any]) -> Dict[str, Any]:
        task_type = task_payload.get("type")
        print(f"CAPITAN CXP: Recibida tarea táctica '{task_type}'.")
        handler = getattr(self, f"_handle_{task_type}", self._handle_unknown)
        return handler(task_payload)

    def _handle_registrar_factura_proveedor(self, task_data: Dict[str, Any]) -> Dict[str, Any]:
        """
        Registra una nueva factura de un proveedor en el sistema de cuentas por pagar.
        """
        proveedor_id = task_data.get("proveedor_id")
        monto = task_data.get("monto")
        fecha_vencimiento_str = task_data.get("fecha_vencimiento")

        if not all([proveedor_id, monto, fecha_vencimiento_str]):
            return {"status": "FAILED", "error": "Faltan datos: proveedor_id, monto y fecha_vencimiento son requeridos."}

        try:
            monto_decimal = Decimal(str(monto))
            fecha_vencimiento = date.fromisoformat(fecha_vencimiento_str)
        except (ValueError, TypeError):
            return {"status": "FAILED", "error": "Formato de monto o fecha inválido."}

        factura_id = f"CXP-{uuid.uuid4().hex[:8].upper()}"
        CUENTAS_POR_PAGAR_DB[factura_id] = {
            "id": factura_id,
            "proveedor_id": proveedor_id,
            "monto": monto_decimal,
            "fecha_vencimiento": fecha_vencimiento,
            "estado": "PENDIENTE", # PENDIENTE, PAGADA
            "fecha_registro": datetime.utcnow().isoformat()
        }

        print(f"CAPITAN CXP: Factura '{factura_id}' de '${monto_decimal}' registrada para proveedor '{proveedor_id}'.")
        return {"status": "COMPLETED", "result": {"factura_id": factura_id}}

    def _handle_programar_pago_factura(self, task_data: Dict[str, Any]) -> Dict[str, Any]:
        """
        Marca una factura como pagada. En un sistema real, esto iniciaría un
        flujo de pago y generaría un asiento contable.
        """
        factura_id = task_data.get("factura_id")

        if factura_id not in CUENTAS_POR_PAGAR_DB:
            return {"status": "FAILED", "error": f"Factura '{factura_id}' no encontrada."}

        factura = CUENTAS_POR_PAGAR_DB[factura_id]
        if factura["estado"] == "PAGADA":
            return {"status": "FAILED", "error": f"La factura '{factura_id}' ya fue pagada."}

        print(f"CAPITAN CXP: Pagando factura '{factura_id}' por un monto de '${factura['monto']}'.")
        factura["estado"] = "PAGADA"
        factura["fecha_pago"] = datetime.utcnow().isoformat()

        # Simulación de la creación del asiento contable correspondiente
        print("  -> Tarea secundaria: Generar asiento contable de egreso.")

        return {"status": "COMPLETED", "result": {"factura_id": factura_id, "estado": "PAGADA"}}

    def _handle_unknown(self, task_data: Dict[str, Any]) -> Dict[str, Any]:
        return {"status": "FAILED", "error": "Tarea de Cuentas por Pagar desconocida."}

# Ejemplo de uso
if __name__ == '__main__':
    capitan = CapitanCuentasPorPagar()

    print("--- Caso 1: Registrar nueva factura de proveedor ---")
    tarea1 = {
        "type": "registrar_factura_proveedor",
        "proveedor_id": "PROV-001",
        "monto": "250.75",
        "fecha_vencimiento": "2024-12-15"
    }
    resultado1 = capitan.execute_task(tarea1)
    print("Resultado:", resultado1)
    print("BD Cuentas por Pagar:", CUENTAS_POR_PAGAR_DB)
    print("-" * 20)

    print("\n--- Caso 2: Pagar la factura registrada ---")
    factura_id_a_pagar = resultado1.get("result", {}).get("factura_id")
    tarea2 = {"type": "programar_pago_factura", "factura_id": factura_id_a_pagar}
    resultado2 = capitan.execute_task(tarea2)
    print("Resultado:", resultado2)
    print("BD Cuentas por Pagar (actualizada):")
    import json
    # Custom JSON encoder for Decimal and date objects
    class CustomEncoder(json.JSONEncoder):
        def default(self, obj):
            if isinstance(obj, Decimal):
                return str(obj)
            if isinstance(obj, date):
                return obj.isoformat()
            return json.JSONEncoder.default(self, obj)
    print(json.dumps(CUENTAS_POR_PAGAR_DB, indent=2, cls=CustomEncoder))
    print("-" * 20)
