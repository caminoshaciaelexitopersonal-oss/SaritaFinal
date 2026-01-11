"""
Agente Capitán Táctico: CapitanReportesContables

Responsable de generar informes contables estándar a partir de los
datos registrados en el libro diario.
"""

from typing import Dict, Any, List
from decimal import Decimal

# --- Simulación de Dependencias (Bases de Datos de otros Capitanes) ---

# Libro Diario simulado (de CapitanAsientosContables)
LIBRO_DIARIO_DB = [
    {"id": "AS-001", "descripcion": "Venta tour #1", "total": Decimal("150.00"), "movimientos": [
        {"cuenta": "1105-Caja", "tipo": "DEBITO", "monto": 150.00},
        {"cuenta": "4135-Ingresos", "tipo": "CREDITO", "monto": 150.00}
    ]},
    {"id": "AS-002", "descripcion": "Pago proveedor XYZ", "total": Decimal("75.50"), "movimientos": [
        {"cuenta": "2205-Proveedores", "tipo": "DEBITO", "monto": 75.50},
        {"cuenta": "1110-Bancos", "tipo": "CREDITO", "monto": 75.50}
    ]},
    {"id": "AS-003", "descripcion": "Venta tour #2", "total": Decimal("200.00"), "movimientos": [
        {"cuenta": "1110-Bancos", "tipo": "DEBITO", "monto": 200.00},
        {"cuenta": "4135-Ingresos", "tipo": "CREDITO", "monto": 200.00}
    ]}
]

# --- Fin de Simulación ---

class CapitanReportesContables:
    """
    Ejecuta tareas tácticas de generación de reportes contables.
    """

    def execute_task(self, task_payload: Dict[str, Any]) -> Dict[str, Any]:
        task_type = task_payload.get("type")
        print(f"CAPITAN REPORTES: Recibida tarea táctica '{task_type}'.")
        handler = getattr(self, f"_handle_{task_type}", self._handle_unknown)
        return handler(task_payload)

    def _handle_generar_balance_de_comprobacion(self, task_data: Dict[str, Any]) -> Dict[str, Any]:
        """
        Calcula el balance de saldos de todas las cuentas a partir del libro diario.
        """
        print("CAPITAN REPORTES: Generando Balance de Comprobación.")

        saldos = {}
        for asiento in LIBRO_DIARIO_DB:
            for mov in asiento.get("movimientos", []):
                cuenta = mov.get("cuenta")
                monto = Decimal(str(mov.get("monto", "0.0")))

                if cuenta not in saldos:
                    saldos[cuenta] = {"debitos": Decimal("0.0"), "creditos": Decimal("0.0")}

                if mov.get("tipo") == "DEBITO":
                    saldos[cuenta]["debitos"] += monto
                elif mov.get("tipo") == "CREDITO":
                    saldos[cuenta]["creditos"] += monto

        total_debitos = sum(s["debitos"] for s in saldos.values())
        total_creditos = sum(s["creditos"] for s in saldos.values())

        reporte = {
            "saldos_por_cuenta": saldos,
            "totales": {
                "debitos": total_debitos,
                "creditos": total_creditos
            },
            "verificacion": "OK" if total_debitos == total_creditos else "ERROR: SUMAS NO IGUALES"
        }

        return {"status": "COMPLETED", "result": {"reporte": reporte}}

    def _handle_unknown(self, task_data: Dict[str, Any]) -> Dict[str, Any]:
        return {"status": "FAILED", "error": "Tipo de reporte desconocido."}

# Ejemplo de uso
if __name__ == '__main__':
    capitan = CapitanReportesContables()

    print("--- Generando Balance de Comprobación ---")
    tarea = {"type": "generar_balance_de_comprobacion"}
    resultado = capitan.execute_task(tarea)

    import json
    print("\nResultado del Reporte:")
    # Usamos default=str para manejar los objetos Decimal en la serialización JSON
    print(json.dumps(resultado, indent=2, default=str))
