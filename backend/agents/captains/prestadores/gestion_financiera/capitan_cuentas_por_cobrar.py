"""
Agente Capitán Táctico: CapitanCuentasPorCobrar

Responsable de gestionar las facturas de venta emitidas a clientes,
realizar seguimiento de cobros y aplicar pagos.
"""

from typing import Dict, Any, List
from decimal import Decimal
import uuid
from datetime import datetime, date

# Base de datos simulada de cuentas por cobrar (cartera)
CUENTAS_POR_COBRAR_DB = {}

class CapitanCuentasPorCobrar:
    """
    Ejecuta tareas tácticas de gestión de cuentas por cobrar.
    """

    def execute_task(self, task_payload: Dict[str, Any]) -> Dict[str, Any]:
        task_type = task_payload.get("type")
        print(f"CAPITAN CXC: Recibida tarea táctica '{task_type}'.")
        handler = getattr(self, f"_handle_{task_type}", self._handle_unknown)
        return handler(task_payload)

    def _handle_registrar_factura_cliente(self, task_data: Dict[str, Any]) -> Dict[str, Any]:
        """
        Registra una nueva factura de venta en la cartera de cuentas por cobrar.
        """
        factura_id_venta = task_data.get("factura_id_venta")
        cliente_id = task_data.get("cliente_id")
        monto = task_data.get("monto")
        fecha_vencimiento_str = task_data.get("fecha_vencimiento")

        if not all([factura_id_venta, cliente_id, monto, fecha_vencimiento_str]):
            return {"status": "FAILED", "error": "Faltan datos requeridos."}

        try:
            monto_decimal = Decimal(str(monto))
            fecha_vencimiento = date.fromisoformat(fecha_vencimiento_str)
        except (ValueError, TypeError):
            return {"status": "FAILED", "error": "Formato de monto o fecha inválido."}

        cxc_id = f"CXC-{uuid.uuid4().hex[:8].upper()}"
        CUENTAS_POR_COBRAR_DB[cxc_id] = {
            "id": cxc_id,
            "factura_id_venta": factura_id_venta,
            "cliente_id": cliente_id,
            "monto_total": monto_decimal,
            "saldo_pendiente": monto_decimal,
            "fecha_vencimiento": fecha_vencimiento,
            "estado": "PENDIENTE", # PENDIENTE, PAGADA, VENCIDA
            "fecha_registro": datetime.utcnow().isoformat()
        }

        print(f"CAPITAN CXC: Factura '{factura_id_venta}' de '${monto_decimal}' registrada en cartera.")
        return {"status": "COMPLETED", "result": {"cxc_id": cxc_id}}

    def _handle_aplicar_pago_recibido(self, task_data: Dict[str, Any]) -> Dict[str, Any]:
        """
        Aplica un pago a una cuenta por cobrar, reduciendo el saldo.
        """
        cxc_id = task_data.get("cxc_id")
        monto_pago = task_data.get("monto_pago")

        if cxc_id not in CUENTAS_POR_COBRAR_DB:
            return {"status": "FAILED", "error": f"Cuenta por cobrar '{cxc_id}' no encontrada."}

        cxc = CUENTAS_POR_COBRAR_DB[cxc_id]
        if cxc["estado"] == "PAGADA":
            return {"status": "FAILED", "error": "La cuenta ya está saldada."}

        monto_pago_decimal = Decimal(str(monto_pago))

        if monto_pago_decimal > cxc["saldo_pendiente"]:
             return {"status": "FAILED", "error": "El pago excede el saldo pendiente."}

        print(f"CAPITAN CXC: Aplicando pago de '${monto_pago_decimal}' a la cuenta '{cxc_id}'.")
        cxc["saldo_pendiente"] -= monto_pago_decimal

        if cxc["saldo_pendiente"] == 0:
            cxc["estado"] = "PAGADA"
            print(f"  -> La cuenta '{cxc_id}' ha sido saldada.")

        return {"status": "COMPLETED", "result": {"cxc_id": cxc_id, "nuevo_saldo": cxc["saldo_pendiente"]}}

    def _handle_consultar_estado_cartera(self, task_data: Dict[str, Any]) -> Dict[str, Any]:
        """Consulta y retorna un resumen del estado de la cartera."""
        print("CAPITAN CXC: Generando reporte de estado de cartera.")

        total_pendiente = Decimal('0.0')
        total_vencido = Decimal('0.0')
        hoy = date.today()

        for cxc in CUENTAS_POR_COBRAR_DB.values():
            if cxc["estado"] == "PENDIENTE":
                total_pendiente += cxc["saldo_pendiente"]
                if cxc["fecha_vencimiento"] < hoy:
                    total_vencido += cxc["saldo_pendiente"]
                    cxc["estado"] = "VENCIDA" # Actualiza estado si está vencida

        reporte = {
            "total_cartera_pendiente": total_pendiente,
            "total_cartera_vencida": total_vencido,
            "cantidad_facturas_pendientes": len([c for c in CUENTAS_POR_COBRAR_DB.values() if c["estado"] != "PAGADA"])
        }
        return {"status": "COMPLETED", "result": {"reporte_cartera": reporte}}


    def _handle_unknown(self, task_data: Dict[str, Any]) -> Dict[str, Any]:
        return {"status": "FAILED", "error": "Tarea de Cuentas por Cobrar desconocida."}

# Ejemplo de uso
if __name__ == '__main__':
    capitan = CapitanCuentasPorCobrar()

    print("--- Caso 1: Registrar nueva factura de cliente ---")
    tarea1 = {
        "type": "registrar_factura_cliente",
        "factura_id_venta": "FV-2024-001", "cliente_id": "CLI-123",
        "monto": "500.00", "fecha_vencimiento": "2023-12-31" # Vencida
    }
    resultado1 = capitan.execute_task(tarea1)
    cxc_id_1 = resultado1["result"]["cxc_id"]
    print("-" * 20)

    tarea2 = {
        "type": "registrar_factura_cliente",
        "factura_id_venta": "FV-2024-002", "cliente_id": "CLI-456",
        "monto": "1000.00", "fecha_vencimiento": "2025-01-31" # Vigente
    }
    capitan.execute_task(tarea2)
    print("-" * 20)

    print("\n--- Caso 2: Aplicar un pago parcial ---")
    tarea3 = {"type": "aplicar_pago_recibido", "cxc_id": cxc_id_1, "monto_pago": "200.00"}
    capitan.execute_task(tarea3)
    print("-" * 20)

    print("\n--- Caso 3: Consultar estado de cartera ---")
    import json
    class CustomEncoder(json.JSONEncoder):
        def default(self, obj):
            if isinstance(obj, Decimal): return str(obj)
            if isinstance(obj, date): return obj.isoformat()
            return json.JSONEncoder.default(self, obj)

    resultado_cartera = capitan.execute_task({"type": "consultar_estado_cartera"})
    print(json.dumps(resultado_cartera, indent=2, cls=CustomEncoder))

    print("\nBD Cuentas por Cobrar (final):")
    print(json.dumps(CUENTAS_POR_COBRAR_DB, indent=2, cls=CustomEncoder))
    print("-" * 20)
