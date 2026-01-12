from typing import Dict, Any

class CapitanPlanificacionFinanciera:
    """
    Misión: Desarrollar modelos y proyecciones financieras a largo plazo para
    apoyar la toma de decisiones estratégicas, como inversiones o expansión.
    """

    def __init__(self, coronel):
        self.coronel = coronel
        self.context = {}
        print(f"CAPITÁN PLANIFICACIÓN FINANCIERA: Inicializado.")

    def handle_order(self, order: Dict[str, Any]) -> Dict[str, Any]:
        """
        Recibe órdenes para modelar un escenario financiero futuro.
        """
        print(f"CAPITÁN PLANIFICACIÓN FINANCIERA: Orden recibida - {order['type']}")
        self.context['current_order'] = order

        plan = self.plan()
        delegation_results = self.delegate(plan)
        report = self.report(delegation_results)

        return report

    def plan(self) -> Dict[str, Any]:
        """
        Crea un plan para construir el modelo financiero.
        """
        print("CAPITÁN PLANIFICACIÓN FINANCIERA: Creando plan de modelado...")
        scenario = self.context.get('current_order', {}).get('details', {}).get('scenario', 'base')

        planned_steps = {
            "step_1": f"definir_supuestos_clave_para_escenario_{scenario}",
            "step_2": "recopilar_datos_historicos_y_de_mercado",
            "step_3": "construir_modelo_de_proyeccion_de_estados_financieros",
            "step_4": "realizar_analisis_de_sensibilidad"
        }

        self.context['plan'] = planned_steps
        return planned_steps

    def delegate(self, plan: Dict[str, Any]) -> Dict[str, Any]:
        """
        Delega tareas de modelado y análisis de datos a Tenientes analistas.
        """
        print("CAPITÁN PLANIFICACIÓN FINANCIERA: Delegando tareas de modelado...")
        results = {}
        for step, task in plan.items():
            print(f"  - Delegando tarea: {task}")
            results[step] = {"status": "DELEGATED", "result": f"Tarea '{task}' delegada para ejecución."}

        self.context['delegation_results'] = results
        return results

    def report(self, delegation_results: Dict[str, Any]) -> Dict[str, Any]:
        """
        Reporta los resultados del modelo financiero y las proyecciones.
        """
        print("CAPITÁN PLANIFICACIÓN FINANCIERA: Preparando informe de proyecciones...")

        report = {
            "captain": self.__class__.__name__,
            "order_id": self.context.get('current_order', {}).get('id', 'N/A'),
            "status": "SUCCESS",
            "result": {
                "message": "Modelado financiero completado.",
                "projection_highlight": "El escenario de expansión muestra un VAN positivo a 5 años." # Simulado
            }
        }

        print("CAPITÁN PLANIFICACIÓN FINANCIERA: Informe de proyecciones listo.")
        return report
