from typing import Dict, Any

class CapitanRiesgoFinanciero:
    """
    Misión: Identificar, evaluar y mitigar los riesgos financieros que pueden
    afectar a la empresa, como el riesgo de mercado, crédito y liquidez.
    """

    def __init__(self, coronel):
        self.coronel = coronel
        self.context = {}
        print(f"CAPITÁN RIESGO FINANCIERO: Inicializado.")

    def handle_order(self, order: Dict[str, Any]) -> Dict[str, Any]:
        """
        Recibe órdenes para evaluar un riesgo específico o el perfil de riesgo general.
        """
        print(f"CAPITÁN RIESGO FINANCIERO: Orden recibida - {order['type']}")
        self.context['current_order'] = order

        plan = self.plan()
        delegation_results = self.delegate(plan)
        report = self.report(delegation_results)

        return report

    def plan(self) -> Dict[str, Any]:
        """
        Crea un plan para la evaluación del riesgo.
        """
        print("CAPITÁN RIESGO FINANCIERO: Creando plan de evaluación de riesgo...")
        risk_type = self.context.get('current_order', {}).get('details', {}).get('risk_type', 'general')

        planned_steps = {
            "step_1": f"identificar_factores_de_riesgo_para_{risk_type}",
            "step_2": "cuantificar_exposicion_y_potencial_impacto",
            "step_3": "desarrollar_estrategias_de_mitigacion",
            "step_4": "establecer_indicadores_clave_de_riesgo_kri"
        }

        self.context['plan'] = planned_steps
        return planned_steps

    def delegate(self, plan: Dict[str, Any]) -> Dict[str, Any]:
        """
        Delega tareas de análisis de datos y modelado de riesgos a Tenientes especialistas.
        """
        print("CAPITÁN RIESGO FINANCIERO: Delegando tareas de análisis de riesgo...")
        results = {}
        for step, task in plan.items():
            print(f"  - Delegando tarea: {task}")
            results[step] = {"status": "DELEGATED", "result": f"Tarea '{task}' delegada para ejecución."}

        self.context['delegation_results'] = results
        return results

    def report(self, delegation_results: Dict[str, Any]) -> Dict[str, Any]:
        """
        Reporta el perfil de riesgo y las estrategias de mitigación recomendadas.
        """
        print("CAPITÁN RIESGO FINANCIERO: Preparando informe de riesgo...")

        report = {
            "captain": self.__class__.__name__,
            "order_id": self.context.get('current_order', {}).get('id', 'N/A'),
            "status": "SUCCESS",
            "result": {
                "message": "Evaluación de riesgo completada.",
                "risk_profile": "MODERADO",
                "mitigation_plan": "Diversificar cartera de inversiones para reducir riesgo de mercado." # Simulado
            }
        }

        print("CAPITÁN RIESGO FINANCIERO: Informe de riesgo listo.")
        return report
