from typing import Dict, Any

class CapitanPlanificacionRegional:
    """
    Misión: Orquestar la planificación turística a nivel departamental,
    alineando las estrategias de los municipios y desarrollando planes
    regionales que potencien los atractivos del departamento.
    """

    def __init__(self, coronel):
        self.coronel = coronel
        self.context = {}
        print(f"CAPITÁN PLANIFICACIÓN REGIONAL: Inicializado.")

    def handle_order(self, order: Dict[str, Any]) -> Dict[str, Any]:
        """
        Recibe órdenes para crear o actualizar el plan de desarrollo turístico regional.
        """
        print(f"CAPITÁN PLANIFICACIÓN REGIONAL: Orden recibida - {order['type']}")
        self.context['current_order'] = order

        plan = self.plan()
        delegation_results = self.delegate(plan)
        report = self.report(delegation_results)

        return report

    def plan(self) -> Dict[str, Any]:
        """
        Crea un plan de trabajo para el desarrollo del plan regional.
        """
        print("CAPITÁN PLANIFICACIÓN REGIONAL: Creando plan de desarrollo regional...")
        plan_period = self.context.get('current_order', {}).get('details', {}).get('period')

        planned_steps = {
            "step_1": f"analizar_diagnostico_turistico_actual_del_departamento",
            "step_2": "delegar_mesas_de_trabajo_a_CapitanCoordinacionMunicipal",
            "step_3": f"definir_ejes_estrategicos_para_el_periodo_{plan_period}",
            "step_4": "estructurar_el_documento_del_plan_regional"
        }

        self.context['plan'] = planned_steps
        return planned_steps

    def delegate(self, plan: Dict[str, Any]) -> Dict[str, Any]:
        """
        Delega la coordinación con municipios a su capitán especialista.
        """
        print("CAPITÁN PLANIFICACIÓN REGIONAL: Delegando tareas de coordinación...")
        results = {}
        for step, task in plan.items():
            print(f"  - Delegando tarea: {task}")
            results[step] = {"status": "DELEGATED", "result": f"Tarea '{task}' delegada para ejecución."}

        self.context['delegation_results'] = results
        return results

    def report(self, delegation_results: Dict[str, Any]) -> Dict[str, Any]:
        """
        Reporta la finalización del plan de desarrollo turístico regional.
        """
        print("CAPITÁN PLANIFICACIÓN REGIONAL: Preparando informe del plan...")

        report = {
            "captain": self.__class__.__name__,
            "order_id": self.context.get('current_order', {}).get('id', 'N/A'),
            "status": "SUCCESS",
            "result": {
                "message": "Plan de Desarrollo Turístico Regional generado.",
                "plan_location": "/path/to/plan_regional.pdf" # Simulado
            }
        }

        print("CAPITÁN PLANIFICACIÓN REGIONAL: Informe del plan listo.")
        return report
