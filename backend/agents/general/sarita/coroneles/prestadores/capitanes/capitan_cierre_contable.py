from typing import Dict, Any

class CapitanCierreContable:
    """
    Misión: Ejecutar los procedimientos técnicos del cierre de un período contable
    (mensual, anual), como el cálculo de amortizaciones, depreciaciones y ajustes.
    """

    def __init__(self, coronel):
        self.coronel = coronel
        self.context = {}
        print(f"CAPITÁN CIERRE CONTABLE: Inicializado.")

    def handle_order(self, order: Dict[str, Any]) -> Dict[str, Any]:
        """
        Recibe la orden de iniciar el proceso de cierre para un período específico.
        """
        print(f"CAPITÁN CIERRE CONTABLE: Orden recibida - {order['type']}")
        self.context['current_order'] = order

        plan = self.plan()
        delegation_results = self.delegate(plan)
        report = self.report(delegation_results)

        return report

    def plan(self) -> Dict[str, Any]:
        """
        Crea un plan de cierre detallado con todos los pasos técnicos.
        """
        print("CAPITÁN CIERRE CONTABLE: Creando plan de cierre de período...")
        periodo = self.context.get('current_order', {}).get('details', {}).get('periodo')

        planned_steps = {
            "step_1": f"calcular_depreciacion_de_activos_para_{periodo}",
            "step_2": f"registrar_amortizacion_de_intangibles_para_{periodo}",
            "step_3": "realizar_ajustes_por_inflacion_si_aplica",
            "step_4": "cerrar_cuentas_nominales_y_trasladar_a_resultados"
        }

        self.context['plan'] = planned_steps
        return planned_steps

    def delegate(self, plan: Dict[str, Any]) -> Dict[str, Any]:
        """
        Delega la ejecución de cálculos específicos a Tenientes contables.
        """
        print("CAPITÁN CIERRE CONTABLE: Delegando tareas de cierre...")
        results = {}
        for step, task in plan.items():
            print(f"  - Delegando tarea: {task}")
            results[step] = {"status": "DELEGATED", "result": f"Tarea '{task}' delegada para ejecución."}

        self.context['delegation_results'] = results
        return results

    def report(self, delegation_results: Dict[str, Any]) -> Dict[str, Any]:
        """
        Reporta la finalización del cierre técnico al Capitán General Contable.
        """
        print("CAPITÁN CIERRE CONTABLE: Preparando informe de cierre técnico...")

        report = {
            "captain": self.__class__.__name__,
            "order_id": self.context.get('current_order', {}).get('id', 'N/A'),
            "status": "SUCCESS",
            "result": {
                "message": "Cierre técnico del período completado exitosamente."
            }
        }

        print("CAPITÁN CIERRE CONTABLE: Informe de cierre listo.")
        return report
