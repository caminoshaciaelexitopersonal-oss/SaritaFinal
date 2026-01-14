from typing import Dict, Any

class CapitanContabilidadGeneral:
    """
    Misión: Orquestar el ciclo contable completo, asegurando la integridad
    de los registros, el cumplimiento normativo y la correcta generación
    de informes financieros.
    """

    def __init__(self, coronel):
        self.coronel = coronel
        self.context = {}
        print(f"CAPITÁN CONTABILIDAD GENERAL: Inicializado.")

    def handle_order(self, order: Dict[str, Any]) -> Dict[str, Any]:
        """
        Recibe órdenes de alto nivel, como 'ejecutar cierre mensual'.
        """
        print(f"CAPITÁN CONTABILIDAD GENERAL: Orden recibida - {order['type']}")
        self.context['current_order'] = order

        plan = self.plan()
        delegation_results = self.delegate(plan)
        report = self.report(delegation_results)

        return report

    def plan(self) -> Dict[str, Any]:
        """
        Crea un plan para ejecutar un proceso contable complejo.
        """
        print("CAPITÁN CONTABILIDAD GENERAL: Creando plan de proceso contable...")
        order_type = self.context.get('current_order', {}).get('type')

        planned_steps = {}
        if order_type == "ejecutar_cierre_contable":
            planned_steps = {
                "step_1": "delegar_verificacion_de_asientos_a_CapitanCumplimiento",
                "step_2": "delegar_ejecucion_de_cierre_a_CapitanCierreContable",
                "step_3": "delegar_generacion_de_informes_a_CapitanReportesContables"
            }

        self.context['plan'] = planned_steps
        return planned_steps

    def delegate(self, plan: Dict[str, Any]) -> Dict[str, Any]:
        """
        Delega tareas específicas a los capitanes contables especialistas.
        """
        print("CAPITÁN CONTABILIDAD GENERAL: Delegando tareas a Capitanes Contables...")
        results = {}
        for step, task in plan.items():
            print(f"  - Delegando tarea: {task}")
            results[step] = {"status": "DELEGATED_TO_CAPTAIN", "result": f"Tarea '{task}' delegada exitosamente."}

        self.context['delegation_results'] = results
        return results

    def report(self, delegation_results: Dict[str, Any]) -> Dict[str, Any]:
        """
        Reporta la finalización del proceso contable al Coronel.
        """
        print("CAPITÁN CONTABILIDAD GENERAL: Preparando informe de estado contable...")

        report = {
            "captain": self.__class__.__name__,
            "order_id": self.context.get('current_order', {}).get('id', 'N/A'),
            "status": "SUCCESS",
            "summary": f"Proceso contable '{self.context.get('current_order', {}).get('type')}' completado.",
            "details": delegation_results
        }

        print("CAPITÁN CONTABILIDAD GENERAL: Informe contable listo.")
        return report
