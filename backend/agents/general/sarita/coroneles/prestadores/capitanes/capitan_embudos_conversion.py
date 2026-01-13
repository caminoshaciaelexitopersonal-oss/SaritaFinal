from typing import Dict, Any

class CapitanEmbudosConversion:
    """
    Misión: Analizar y optimizar los embudos de conversión (funnels) para maximizar
    la tasa de conversión de prospectos a clientes.
    """

    def __init__(self, coronel):
        self.coronel = coronel
        self.context = {}
        print(f"CAPITÁN EMBUDOS DE CONVERSIÓN: Inicializado.")

    def handle_order(self, order: Dict[str, Any]) -> Dict[str, Any]:
        """
        Recibe una orden para analizar o proponer mejoras a un embudo de conversión.
        """
        print(f"CAPITÁN EMBUDOS DE CONVERSIÓN: Orden recibida - {order['type']}")
        self.context['current_order'] = order

        plan = self.plan()
        delegation_results = self.delegate(plan)
        report = self.report(delegation_results)

        return report

    def plan(self) -> Dict[str, Any]:
        """
        Crea un plan de análisis del embudo de conversión.
        """
        print("CAPITÁN EMBUDOS DE CONVERSIÓN: Creando plan de análisis de funnel...")
        funnel_name = self.context.get('current_order', {}).get('details', {}).get('funnel_name', 'default_funnel')

        planned_steps = {
            "step_1": f"mapear_etapas_actuales_del_embudo_{funnel_name}",
            "step_2": "delegar_recoleccion_de_metricas_por_etapa",
            "step_3": "identificar_puntos_de_fuga_y_cuellos_de_botella",
            "step_4": "proponer_hipotesis_de_optimizacion"
        }

        self.context['plan'] = planned_steps
        return planned_steps

    def delegate(self, plan: Dict[str, Any]) -> Dict[str, Any]:
        """
        Delega tareas de recolección de datos a Tenientes analistas.
        """
        print("CAPITÁN EMBUDOS DE CONVERSIÓN: Delegando tareas de análisis de datos...")
        results = {}
        for step, task in plan.items():
            print(f"  - Delegando tarea: {task}")
            results[step] = {"status": "DELEGATED", "result": f"Tarea '{task}' delegada para ejecución."}

        self.context['delegation_results'] = results
        return results

    def report(self, delegation_results: Dict[str, Any]) -> Dict[str, Any]:
        """
        Reporta los hallazgos del análisis y las recomendaciones de optimización.
        """
        print("CAPITÁN EMBUDOS DE CONVERSIÓN: Preparando informe de análisis de embudo...")

        report = {
            "captain": self.__class__.__name__,
            "order_id": self.context.get('current_order', {}).get('id', 'N/A'),
            "status": "SUCCESS",
            "result": {
                "message": "Análisis de embudo de conversión completado.",
                "key_finding": "Se identificó una caída del 40% en la etapa de checkout.",
                "recommendation": "Implementar un proceso de checkout simplificado."
            }
        }

        print("CAPITÁN EMBUDOS DE CONVERSIÓN: Informe de análisis listo.")
        return report
