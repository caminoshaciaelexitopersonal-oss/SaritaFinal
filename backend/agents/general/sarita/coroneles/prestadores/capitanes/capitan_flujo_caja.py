from typing import Dict, Any

class CapitanFlujoCaja:
    """
    Misión: Monitorear, analizar y proyectar el flujo de caja de la empresa
    para garantizar la liquidez y la capacidad de cumplir con las obligaciones.
    """

    def __init__(self, coronel):
        self.coronel = coronel
        self.context = {}
        print(f"CAPITÁN FLUJO DE CAJA: Inicializado.")

    def handle_order(self, order: Dict[str, Any]) -> Dict[str, Any]:
        """
        Recibe órdenes para analizar el estado de flujo de caja o proyectar escenarios.
        """
        print(f"CAPITÁN FLUJO DE CAJA: Orden recibida - {order['type']}")
        self.context['current_order'] = order

        plan = self.plan()
        delegation_results = self.delegate(plan)
        report = self.report(delegation_results)

        return report

    def plan(self) -> Dict[str, Any]:
        """
        Crea un plan para analizar el flujo de caja.
        """
        print("CAPITÁN FLUJO DE CAJA: Creando plan de análisis de liquidez...")
        projection_months = self.context.get('current_order', {}).get('details', {}).get('months', 3)

        planned_steps = {
            "step_1": "recopilar_datos_de_ingresos_y_egresos_historicos",
            "step_2": f"proyectar_flujo_de_caja_a_{projection_months}_meses",
            "step_3": "identificar_posibles_deficit_o_superavit_de_caja",
            "step_4": "preparar_recomendaciones_de_accion"
        }

        self.context['plan'] = planned_steps
        return planned_steps

    def delegate(self, plan: Dict[str, Any]) -> Dict[str, Any]:
        """
        Delega tareas de recolección de datos y modelado a Tenientes analistas.
        """
        print("CAPITÁN FLUJO DE CAJA: Delegando tareas de análisis de datos...")
        results = {}
        for step, task in plan.items():
            print(f"  - Delegando tarea: {task}")
            results[step] = {"status": "DELEGATED", "result": f"Tarea '{task}' delegada para ejecución."}

        self.context['delegation_results'] = results
        return results

    def report(self, delegation_results: Dict[str, Any]) -> Dict[str, Any]:
        """
        Reporta el estado actual y proyectado del flujo de caja.
        """
        print("CAPITÁN FLUJO DE CAJA: Preparando informe de flujo de caja...")

        report = {
            "captain": self.__class__.__name__,
            "order_id": self.context.get('current_order', {}).get('id', 'N/A'),
            "status": "SUCCESS",
            "result": {
                "message": "Análisis de flujo de caja completado.",
                "projection_summary": "Se proyecta superávit de caja para los próximos 3 meses." # Simulado
            }
        }

        print("CAPITÁN FLUJO DE CAJA: Informe de liquidez listo.")
        return report
