"""
Agente Capitán Táctico: CapitanAsientosContables

Responsable de ejecutar la tarea atómica de registrar asientos contables
en el libro diario, asegurando el principio de partida doble.
"""

from typing import Dict, Any, List
from decimal import Decimal
import uuid
from datetime import datetime

# Base de datos simulada del libro diario
LIBRO_DIARIO_DB = []

class CapitanAsientosContables:
    """
    Ejecuta tareas tácticas de contabilidad general.
    """

    def execute_task(self, task_payload: Dict[str, Any]) -> Dict[str, Any]:
        task_type = task_payload.get("type")
        print(f"CAPITAN CONTABILIDAD: Recibida tarea táctica '{task_type}'.")
        handler = getattr(self, f"_handle_{task_type}", self._handle_unknown)
        return handler(task_payload)

    def _handle_registrar_asiento_contable(self, task_data: Dict[str, Any]) -> Dict[str, Any]:
        """
        Registra un nuevo asiento contable validando que esté balanceado.
        Un asiento es una lista de movimientos, cada uno con 'cuenta', 'tipo' (DEBITO/CREDITO) y 'monto'.
        """
        movimientos = task_data.get("movimientos", [])
        descripcion = task_data.get("descripcion", "Sin descripción")

        if not movimientos or len(movimientos) < 2:
            return {"status": "FAILED", "error": "Un asiento debe tener al menos dos movimientos."}

        total_debitos = Decimal('0.0')
        total_creditos = Decimal('0.0')

        for mov in movimientos:
            monto = Decimal(str(mov.get('monto', '0.0')))
            if mov.get('tipo') == 'DEBITO':
                total_debitos += monto
            elif mov.get('tipo') == 'CREDITO':
                total_creditos += monto

        # Validación de partida doble
        if total_debitos != total_creditos:
            return {
                "status": "FAILED",
                "error": f"Asiento desbalanceado. Débitos: {total_debitos}, Créditos: {total_creditos}"
            }

        if total_debitos == 0:
            return {"status": "FAILED", "error": "El monto total del asiento no puede ser cero."}

        asiento_id = f"AS-{uuid.uuid4().hex[:8].upper()}"
        nuevo_asiento = {
            "id": asiento_id,
            "timestamp": datetime.utcnow().isoformat(),
            "descripcion": descripcion,
            "total": total_debitos,
            "movimientos": movimientos
        }

        LIBRO_DIARIO_DB.append(nuevo_asiento)
        print(f"CAPITAN CONTABILIDAD: Asiento '{asiento_id}' de '${total_debitos}' registrado: {descripcion}.")

        return {"status": "COMPLETED", "result": {"asiento_id": asiento_id}}

    def _handle_unknown(self, task_data: Dict[str, Any]) -> Dict[str, Any]:
        return {"status": "FAILED", "error": "Tarea contable desconocida."}

# Ejemplo de uso
if __name__ == '__main__':
    capitan = CapitanAsientosContables()

    print("--- Caso 1: Asiento de Venta Balanceado ---")
    tarea1 = {
        "type": "registrar_asiento_contable",
        "descripcion": "Venta de tour al contado",
        "movimientos": [
            {"cuenta": "1105-Caja", "tipo": "DEBITO", "monto": 150.00},
            {"cuenta": "4135-IngresosOperacionales", "tipo": "CREDITO", "monto": 150.00}
        ]
    }
    resultado1 = capitan.execute_task(tarea1)
    print("Resultado:", resultado1)
    print("-" * 20)

    print("\n--- Caso 2: Asiento de Gasto con Múltiples Movimientos ---")
    tarea2 = {
        "type": "registrar_asiento_contable",
        "descripcion": "Pago de salario y retenciones",
        "movimientos": [
            {"cuenta": "5105-GastosDePersonal", "tipo": "DEBITO", "monto": 1200.00},
            {"cuenta": "2370-Retenciones", "tipo": "CREDITO", "monto": 120.00},
            {"cuenta": "1110-Bancos", "tipo": "CREDITO", "monto": 1080.00}
        ]
    }
    resultado2 = capitan.execute_task(tarea2)
    print("Resultado:", resultado2)
    print("-" * 20)

    print("\n--- Caso 3: Asiento Desbalanceado (Falla) ---")
    tarea3 = {
        "type": "registrar_asiento_contable",
        "descripcion": "Error en registro",
        "movimientos": [
            {"cuenta": "1105-Caja", "tipo": "DEBITO", "monto": 100.00},
            {"cuenta": "4135-Ingresos", "tipo": "CREDITO", "monto": 99.00}
        ]
    }
    resultado3 = capitan.execute_task(tarea3)
    print("Resultado:", resultado3)
    print("-" * 20)

    print("\n--- Libro Diario Final ---")
    print(LIBRO_DIARIO_DB)
