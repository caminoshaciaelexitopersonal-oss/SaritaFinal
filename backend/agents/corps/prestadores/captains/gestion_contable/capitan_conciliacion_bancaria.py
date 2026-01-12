"""
Agente Capitán Táctico: CapitanConciliacionBancaria

Responsable de comparar los movimientos del libro diario con los extractos
bancarios para identificar discrepancias.
"""

from typing import Dict, Any, List
from decimal import Decimal

# --- Simulación de Dependencias (Bases de Datos de otros Capitanes) ---

# Libro Diario simulado (de CapitanAsientosContables)
LIBRO_DIARIO_DB = [
    {"id": "AS-001", "descripcion": "Venta tour #1", "total": Decimal("150.00"), "movimientos": [{"cuenta": "1110-Bancos", "tipo": "DEBITO", "monto": 150.00}]},
    {"id": "AS-002", "descripcion": "Pago proveedor XYZ", "total": Decimal("75.50"), "movimientos": [{"cuenta": "1110-Bancos", "tipo": "CREDITO", "monto": 75.50}]},
    {"id": "AS-003", "descripcion": "Venta tour #2", "total": Decimal("200.00"), "movimientos": [{"cuenta": "1110-Bancos", "tipo": "DEBITO", "monto": 200.00}]}
]

# --- Fin de Simulación ---

class CapitanConciliacionBancaria:
    """
    Ejecuta tareas tácticas de conciliación bancaria.
    """

    def execute_task(self, task_payload: Dict[str, Any]) -> Dict[str, Any]:
        task_type = task_payload.get("type")
        print(f"CAPITAN CONCILIACION: Recibida tarea táctica '{task_type}'.")
        handler = getattr(self, f"_handle_{task_type}", self._handle_unknown)
        return handler(task_payload)

    def _handle_ejecutar_conciliacion(self, task_data: Dict[str, Any]) -> Dict[str, Any]:
        """
        Compara un extracto bancario con los movimientos de la cuenta 'Bancos' en el libro diario.
        """
        extracto_bancario = task_data.get("extracto", [])
        if not extracto_bancario:
            return {"status": "FAILED", "error": "El extracto bancario está vacío."}

        print(f"CAPITAN CONCILIACION: Iniciando conciliación con {len(extracto_bancario)} transacciones bancarias.")

        movimientos_banco = {f"{t['id']}": Decimal(str(t['monto'])) for t in extracto_bancario}

        movimientos_libro_diario = {}
        for asiento in LIBRO_DIARIO_DB:
            for mov in asiento.get("movimientos", []):
                if mov.get("cuenta") == "1110-Bancos":
                    monto = Decimal(str(mov.get("monto", "0.0")))
                    # Usamos el ID del asiento como referencia para la conciliación
                    movimientos_libro_diario[asiento["id"]] = monto if mov["tipo"] == "DEBITO" else -monto

        # --- Lógica de Comparación ---
        transacciones_no_en_libro = []
        discrepancias_monto = []

        for tx_id, monto_banco in movimientos_banco.items():
            if tx_id not in movimientos_libro_diario:
                transacciones_no_en_libro.append({"id": tx_id, "monto": monto_banco})
            elif movimientos_libro_diario[tx_id] != monto_banco:
                discrepancias_monto.append({
                    "id": tx_id,
                    "monto_banco": monto_banco,
                    "monto_libro": movimientos_libro_diario[tx_id]
                })

        asientos_no_en_banco = [
            {"id": asiento_id, "monto": monto_libro}
            for asiento_id, monto_libro in movimientos_libro_diario.items()
            if asiento_id not in movimientos_banco
        ]

        reporte = {
            "transacciones_no_contabilizadas": transacciones_no_en_libro,
            "asientos_no_en_extracto": asientos_no_en_banco,
            "discrepancias_de_monto": discrepancias_monto
        }

        return {"status": "COMPLETED", "result": {"reporte_conciliacion": reporte}}

    def _handle_unknown(self, task_data: Dict[str, Any]) -> Dict[str, Any]:
        return {"status": "FAILED", "error": "Tarea de conciliación desconocida."}

# Ejemplo de uso
if __name__ == '__main__':
    capitan = CapitanConciliacionBancaria()

    # Extracto bancario simulado. Nótese las discrepancias con LIBRO_DIARIO_DB
    extracto_ejemplo = [
        {"id": "AS-001", "monto": 150.00}, # Coincide
        {"id": "AS-002", "monto": -70.00}, # Monto incorrecto
        # Falta AS-003
        {"id": "TX-BANK-999", "monto": 30.00} # Transacción no registrada en libro
    ]

    print("--- Ejecutando Conciliación Bancaria ---")
    tarea = {"type": "ejecutar_conciliacion", "extracto": extracto_ejemplo}
    resultado = capitan.execute_task(tarea)

    import json
    print("Resultado de la Conciliación:")
    print(json.dumps(resultado, indent=2, default=str))
