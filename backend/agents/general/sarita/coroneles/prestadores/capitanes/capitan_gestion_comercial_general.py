from typing import Dict, Any

class CapitanGestionComercialGeneral:
    """
    Misión: Orquestar la estrategia comercial completa, desde la generación de leads
    hasta la conversión y retención, asegurando que todos los capitanes comerciales
    trabajen de forma alineada.
    """

    def __init__(self, coronel):
        self.coronel = coronel
        self.context = {}
        print(f"CAPITÁN GESTIÓN COMERCIAL GENERAL: Inicializado.")

    def handle_order(self, order: Dict[str, Any]) -> Dict[str, Any]:
        """
        Recibe órdenes estratégicas comerciales del Coronel (e.g., 'aumentar ventas 15%').
        """
        print(f"CAPITÁN GESTIÓN COMERCIAL GENERAL: Orden recibida - {order['type']}")
        self.context['current_order'] = order

        plan = self.plan()
        delegation_results = self.delegate(plan)
        report = self.report(delegation_results)

        return report

    def plan(self) -> Dict[str, Any]:
        """
        Crea un plan comercial integrado, asignando objetivos a cada capitán especialista.
        """
        print("CAPITÁN GESTIÓN COMERCIAL GENERAL: Creando plan comercial integrado...")
        order_details = self.context.get('current_order', {}).get('details', {})
        target = order_details.get('target', 'crecimiento_general')

        planned_steps = {
            "step_1": f"delegar_generacion_de_leads_a_CapitanMarketing_con_objetivo_{target}",
            "step_2": "delegar_proceso_de_cierre_a_CapitanVentas",
            "step_3": "delegar_analisis_de_conversion_a_CapitanEmbudosConversion",
            "step_4": "delegar_fidelizacion_a_CapitanRelacionClientes"
        }

        self.context['plan'] = planned_steps
        return planned_steps

    def delegate(self, plan: Dict[str, Any]) -> Dict[str, Any]:
        """
        Delega los sub-objetivos del plan a los Capitanes Comerciales específicos.
        """
        print("CAPITÁN GESTIÓN COMERCIAL GENERAL: Delegando tareas a Capitanes Comerciales...")
        results = {}
        for step, task in plan.items():
            print(f"  - Delegando tarea: {task}")
            results[step] = {"status": "DELEGATED_TO_CAPTAIN", "result": f"Tarea '{task}' delegada exitosamente."}

        self.context['delegation_results'] = results
        return results

    def report(self, delegation_results: Dict[str, Any]) -> Dict[str, Any]:
        """
        Reporta el progreso de la estrategia comercial al Coronel.
        """
        print("CAPITÁN GESTIÓN COMERCIAL GENERAL: Preparando informe de estrategia comercial...")

        report = {
            "captain": self.__class__.__name__,
            "order_id": self.context.get('current_order', {}).get('id', 'N/A'),
            "status": "IN_PROGRESS",
            "summary": f"Estrategia comercial en ejecución con {len(delegation_results)} frentes activos.",
            "details": delegation_results
        }

        print("CAPITÁN GESTIÓN COMERCIAL GENERAL: Informe de estrategia listo.")
        return report
