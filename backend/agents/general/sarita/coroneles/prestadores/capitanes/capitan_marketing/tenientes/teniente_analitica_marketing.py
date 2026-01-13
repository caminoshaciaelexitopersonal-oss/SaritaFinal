from typing import Dict, Any

class TenienteAnaliticaMarketing:
    """
    Rol: Recopilar, procesar y presentar métricas e indicadores de rendimiento
    de las campañas (KPIs).
    Capitán Superior: capitan_marketing
    Tipo de Tareas:
      - recopilar_datos_de_plataformas
      - calcular_cpc_cpl_cpa
      - generar_reporte_de_roi
      - visualizar_datos_en_dashboard
    """
    def __init__(self, capitan):
        self.capitan = capitan

    def execute_task(self, task: Dict[str, Any]) -> Dict[str, Any]:
        print(f"TENIENTE ANALÍTICA MARKETING: Ejecutando tarea {task['type']}")
        return {"status": "SUCCESS", "result": "Tarea de analítica de marketing completada."}
