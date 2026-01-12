from typing import Dict, Any

class CapitanMarketing:
    """
    Misión: Diseñar y ejecutar campañas de marketing para generar prospectos (leads)
    y aumentar la visibilidad de la marca.
    """

    def __init__(self, coronel):
        self.coronel = coronel
        self.context = {}
        print(f"CAPITÁN MARKETING: Inicializado.")

    def handle_order(self, order: Dict[str, Any]) -> Dict[str, Any]:
        """
        Recibe una orden para crear y lanzar una campaña de marketing.
        """
        print(f"CAPITÁN MARKETING: Orden recibida - {order['type']}")
        self.context['current_order'] = order

        plan = self.plan()
        delegation_results = self.delegate(plan)
        report = self.report(delegation_results)

        return report

    def plan(self) -> Dict[str, Any]:
        """
        Crea un plan de campaña, definiendo canales, presupuesto y KPIs.
        """
        print("CAPITÁN MARKETING: Creando plan de campaña...")
        campaign_name = self.context.get('current_order', {}).get('details', {}).get('name', 'nueva_campana')

        planned_steps = {
            "step_1": f"definir_audiencia_objetivo_para_{campaign_name}",
            "step_2": "seleccionar_canales_de_difusion",
            "step_3": "asignar_presupuesto_y_crear_material_grafico",
            "step_4": "establecer_kpis_de_seguimiento"
        }

        self.context['plan'] = planned_steps
        return planned_steps

    def delegate(self, plan: Dict[str, Any]) -> Dict[str, Any]:
        """
        Delega la ejecución de tareas específicas a Tenientes (e.g., Teniente de Redes Sociales).
        """
        print("CAPITÁN MARKETING: Delegando tareas de campaña...")
        results = {}
        for step, task in plan.items():
            print(f"  - Delegando tarea: {task}")
            results[step] = {"status": "DELEGATED", "result": f"Tarea '{task}' delegada para ejecución."}

        self.context['delegation_results'] = results
        return results

    def report(self, delegation_results: Dict[str, Any]) -> Dict[str, Any]:
        """
        Reporta el rendimiento de la campaña al Capitán General Comercial.
        """
        print("CAPITÁN MARKETING: Preparando informe de rendimiento de campaña...")

        report = {
            "captain": self.__class__.__name__,
            "order_id": self.context.get('current_order', {}).get('id', 'N/A'),
            "status": "IN_PROGRESS",
            "result": {
                "message": "Campaña de marketing en ejecución.",
                "current_leads": 0 # Este valor se actualizaría en tiempo real
            }
        }

        print("CAPITÁN MARKETING: Informe de campaña listo.")
        return report
