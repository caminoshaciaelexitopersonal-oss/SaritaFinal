from typing import Dict, Any

class CapitanGestionFinancieraGeneral:
    """
    Misión: Orquestar la estrategia financiera de la empresa, supervisando
    la liquidez, el riesgo y la planificación para asegurar la salud
    financiera y el crecimiento sostenible.
    """

    def __init__(self, coronel):
        self.coronel = coronel
        self.context = {}
        print(f"CAPITÁN GESTIÓN FINANCIERA GENERAL: Inicializado.")

    def handle_order(self, order: Dict[str, Any]) -> Dict[str, Any]:
        """
        Recibe órdenes estratégicas como 'optimizar estructura de capital'.
        """
        print(f"CAPITÁN GESTIÓN FINANCIERA GENERAL: Orden recibida - {order['type']}")
        self.context['current_order'] = order

        plan = self.plan()
        delegation_results = self.delegate(plan)
        report = self.report(delegation_results)

        return report

    def plan(self) -> Dict[str, Any]:
        """
        Crea un plan financiero integrado para cumplir la orden.
        """
        print("CAPITÁN GESTIÓN FINANCIERA GENERAL: Creando plan financiero...")
        order_type = self.context.get('current_order', {}).get('type')

        planned_steps = {}
        if order_type == "evaluar_salud_financiera":
            planned_steps = {
                "step_1": "delegar_analisis_de_liquidez_a_CapitanFlujoCaja",
                "step_2": "delegar_evaluacion_de_exposicion_a_CapitanRiesgoFinanciero",
                "step_3": "delegar_proyeccion_de_escenarios_a_CapitanPlanificacionFinanciera"
            }

        self.context['plan'] = planned_steps
        return planned_steps

    def delegate(self, plan: Dict[str, Any]) -> Dict[str, Any]:
        """
        Delega tareas a los capitanes financieros especialistas.
        """
        print("CAPITÁN GESTIÓN FINANCIERA GENERAL: Delegando tareas a Capitanes Financieros...")
        results = {}
        for step, task in plan.items():
            print(f"  - Delegando tarea: {task}")
            results[step] = {"status": "DELEGATED_TO_CAPTAIN", "result": f"Tarea '{task}' delegada exitosamente."}

        self.context['delegation_results'] = results
        return results

    def report(self, delegation_results: Dict[str, Any]) -> Dict[str, Any]:
        """
        Reporta un diagnóstico financiero consolidado al Coronel.
        """
        print("CAPITÁN GESTIÓN FINANCIERA GENERAL: Preparando informe de diagnóstico financiero...")

        report = {
            "captain": self.__class__.__name__,
            "order_id": self.context.get('current_order', {}).get('id', 'N/A'),
            "status": "SUCCESS",
            "summary": f"Diagnóstico financiero completado.",
            "details": delegation_results
        }

        print("CAPITÁN GESTIÓN FINANCIERA GENERAL: Informe financiero listo.")
        return report
