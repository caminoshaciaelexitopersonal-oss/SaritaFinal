"""
Agente Capitán Táctico: CapitanFlujoDeCaja

Responsable de analizar las cuentas por pagar y por cobrar para generar
proyecciones y reportes de flujo de caja.
"""

from typing import Dict, Any, List
from decimal import Decimal
from datetime import date, timedelta

# --- Simulación de Dependencias (Bases de Datos de otros Capitanes) ---

# Cuentas por Pagar (de CapitanCuentasPorPagar)
CUENTAS_POR_PAGAR_DB = {
    "CXP-001": {"proveedor_id": "PROV-A", "monto": Decimal("300.00"), "fecha_vencimiento": date.today() + timedelta(days=10), "estado": "PENDIENTE"},
    "CXP-002": {"proveedor_id": "PROV-B", "monto": Decimal("500.00"), "fecha_vencimiento": date.today() + timedelta(days=25), "estado": "PENDIENTE"}
}

# Cuentas por Cobrar (de CapitanCuentasPorCobrar)
CUENTAS_POR_COBRAR_DB = {
    "CXC-001": {"cliente_id": "CLI-X", "saldo_pendiente": Decimal("1200.00"), "fecha_vencimiento": date.today() + timedelta(days=5), "estado": "PENDIENTE"},
    "CXC-002": {"cliente_id": "CLI-Y", "saldo_pendiente": Decimal("800.00"), "fecha_vencimiento": date.today() + timedelta(days=40), "estado": "PENDIENTE"}
}

# --- Fin de Simulación ---

class CapitanFlujoDeCaja:
    """
    Ejecuta tareas tácticas de análisis y reporte de flujo de caja.
    """

    def execute_task(self, task_payload: Dict[str, Any]) -> Dict[str, Any]:
        task_type = task_payload.get("type")
        print(f"CAPITAN FLUJO DE CAJA: Recibida tarea táctica '{task_type}'.")
        handler = getattr(self, f"_handle_{task_type}", self._handle_unknown)
        return handler(task_payload)

    def _handle_generar_proyeccion_flujo_de_caja(self, task_data: Dict[str, Any]) -> Dict[str, Any]:
        """
        Proyecta las entradas y salidas de efectivo en un período de tiempo.
        """
        periodo_dias = task_data.get("periodo_dias", 30)
        saldo_inicial = Decimal(str(task_data.get("saldo_inicial_caja", "0.0")))

        print(f"CAPITAN FLUJO DE CAJA: Generando proyección para los próximos {periodo_dias} días.")

        fecha_fin = date.today() + timedelta(days=periodo_dias)

        # Proyección de Entradas (Ingresos)
        entradas_proyectadas = sum(
            cxc["saldo_pendiente"] for cxc in CUENTAS_POR_COBRAR_DB.values()
            if cxc["estado"] == "PENDIENTE" and cxc["fecha_vencimiento"] <= fecha_fin
        )

        # Proyección de Salidas (Egresos)
        salidas_proyectadas = sum(
            cxp["monto"] for cxp in CUENTAS_POR_PAGAR_DB.values()
            if cxp["estado"] == "PENDIENTE" and cxp["fecha_vencimiento"] <= fecha_fin
        )

        flujo_neto = entradas_proyectadas - salidas_proyectadas
        saldo_final_proyectado = saldo_inicial + flujo_neto

        reporte = {
            "periodo_analizado_dias": periodo_dias,
            "saldo_inicial": saldo_inicial,
            "total_entradas_proyectadas": entradas_proyectadas,
            "total_salidas_proyectadas": salidas_proyectadas,
            "flujo_de_caja_neto_proyectado": flujo_neto,
            "saldo_final_de_caja_proyectado": saldo_final_proyectado
        }

        return {"status": "COMPLETED", "result": {"reporte_flujo_caja": reporte}}

    def _handle_unknown(self, task_data: Dict[str, Any]) -> Dict[str, Any]:
        return {"status": "FAILED", "error": "Tarea de Flujo de Caja desconocida."}

# Ejemplo de uso
if __name__ == '__main__':
    capitan = CapitanFlujoDeCaja()

    print("--- Generando Proyección de Flujo de Caja a 30 días ---")
    tarea = {
        "type": "generar_proyeccion_flujo_de_caja",
        "periodo_dias": 30,
        "saldo_inicial_caja": "5000.00"
    }
    resultado = capitan.execute_task(tarea)

    import json
    class CustomEncoder(json.JSONEncoder):
        def default(self, obj):
            if isinstance(obj, Decimal): return str(obj)
            return json.JSONEncoder.default(self, obj)

    print("\nResultado del Reporte:")
    print(json.dumps(resultado, indent=2, cls=CustomEncoder))
