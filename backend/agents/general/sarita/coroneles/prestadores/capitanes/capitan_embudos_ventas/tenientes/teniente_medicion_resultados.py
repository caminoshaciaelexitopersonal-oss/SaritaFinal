from typing import Dict, Any

class TenienteMedicionResultados:
    """
    Rol táctico: Mide y reporta los KPIs generales del embudo de ventas.
    Capitán superior: capitan_embudos_ventas
    Tipo de órdenes que ejecuta:
      - calcular_roi_embudo
      - reportar_costo_por_lead
      - generar_informe_de_rendimiento
    """
    def __init__(self, capitan):
        self.capitan = capitan

    def execute_task(self, task: Dict[str, Any]) -> Dict[str, Any]:
        print(f"TENIENTE MEDICIÓN RESULTADOS: Ejecutando tarea {task['type']}")
        return {"status": "SUCCESS", "result": f"Tarea {task['type']} completada."}
