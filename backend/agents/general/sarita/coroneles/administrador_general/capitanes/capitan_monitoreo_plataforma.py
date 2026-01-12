from typing import Dict, Any

class CapitanMonitoreoPlataforma:
    """
    Misión: Supervisar de forma continua la salud, el rendimiento y el uso
    de recursos de toda la plataforma Sarita, generando alertas tempranas
    ante posibles problemas o degradaciones del servicio.
    """

    def __init__(self, coronel):
        self.coronel = coronel
        self.context = {}
        print(f"CAPITÁN MONITOREO DE PLATAFORMA: Inicializado.")

    def handle_order(self, order: Dict[str, Any]) -> Dict[str, Any]:
        """
        Recibe alertas automáticas de los sistemas de monitoreo o solicitudes
        para generar informes de estado.
        """
        print(f"CAPITÁN MONITOREO DE PLATAFORMA: Orden recibida - {order['type']}")
        self.context['current_order'] = order

        plan = self.plan()
        delegation_results = self.delegate(plan)
        report = self.report(delegation_results)

        return report

    def plan(self) -> Dict[str, Any]:
        """
        Crea un plan para diagnosticar una alerta o generar un informe.
        """
        print("CAPITÁN MONITOREO DE PLATAFORMA: Creando plan de diagnóstico...")
        alert_type = self.context.get('current_order', {}).get('details', {}).get('alert_type')

        planned_steps = {
            "step_1": f"correlacionar_metricas_clave_(cpu_mem_latencia)_para_alerta_{alert_type}",
            "step_2": "delegar_analisis_de_logs_relevantes_a_teniente_sre",
            "step_3": "determinar_causa_raiz_probable_y_componentes_afectados",
            "step_4": "formular_recomendacion_de_accion_inmediata"
        }

        self.context['plan'] = planned_steps
        return planned_steps

    def delegate(self, plan: Dict[str, Any]) -> Dict[str, Any]:
        """
        Delega el análisis técnico a Tenientes de SRE (Site Reliability Engineering).
        """
        print("CAPITÁN MONITOREO DE PLATAFORMA: Delegando tareas de SRE...")
        results = {}
        for step, task in plan.items():
            print(f"  - Delegando tarea: {task}")
            results[step] = {"status": "DELEGATED", "result": f"Tarea '{task}' delegada para ejecución."}

        self.context['delegation_results'] = results
        return results

    def report(self, delegation_results: Dict[str, Any]) -> Dict[str, Any]:
        """
        Reporta el diagnóstico de la plataforma y las acciones recomendadas.
        """
        print("CAPITÁN MONITOREO DE PLATAFORMA: Preparando informe de estado de la plataforma...")

        report = {
            "captain": self.__class__.__name__,
            "order_id": self.context.get('current_order', {}).get('id', 'N/A'),
            "status": "ACTION_REQUIRED",
            "result": {
                "message": "Diagnóstico de alerta de plataforma completado.",
                "root_cause_analysis": "Incremento del 300% en la latencia de la base de datos." # Simulado
            }
        }

        print("CAPITÁN MONITOREO DE PLATAFORMA: Informe de plataforma listo.")
        return report
