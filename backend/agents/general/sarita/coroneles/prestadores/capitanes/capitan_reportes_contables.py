from typing import Dict, Any

class CapitanReportesContables:
    """
    Misión: Generar los estados financieros y otros reportes contables requeridos
    por la dirección o entidades regulatorias.
    """

    def __init__(self, coronel):
        self.coronel = coronel
        self.context = {}
        print(f"CAPITÁN REPORTES CONTABLES: Inicializado.")

    def handle_order(self, order: Dict[str, Any]) -> Dict[str, Any]:
        """
        Recibe una solicitud para generar un reporte contable específico.
        """
        print(f"CAPITÁN REPORTES CONTABLES: Orden recibida - {order['type']}")
        self.context['current_order'] = order

        plan = self.plan()
        delegation_results = self.delegate(plan)
        report = self.report(delegation_results)

        return report

    def plan(self) -> Dict[str, Any]:
        """
        Crea un plan para la generación del reporte, incluyendo la
        recopilación y formato de los datos.
        """
        print("CAPITÁN REPORTES CONTABLES: Creando plan de generación de reporte...")
        report_type = self.context.get('current_order', {}).get('details', {}).get('report_type')

        planned_steps = {
            "step_1": f"extraer_datos_de_cuentas_relevantes_para_{report_type}",
            "step_2": "estructurar_datos_segun_formato_oficial",
            "step_3": "realizar_calculos_y_validaciones_cruzadas",
            "step_4": "generar_documento_final_del_reporte"
        }

        self.context['plan'] = planned_steps
        return planned_steps

    def delegate(self, plan: Dict[str, Any]) -> Dict[str, Any]:
        """
        Delega tareas de extracción y formato de datos a Tenientes analistas.
        """
        print("CAPITÁN REPORTES CONTABLES: Delegando tareas de generación de reportes...")
        results = {}
        for step, task in plan.items():
            print(f"  - Delegando tarea: {task}")
            results[step] = {"status": "DELEGATED", "result": f"Tarea '{task}' delegada para ejecución."}

        self.context['delegation_results'] = results
        return results

    def report(self, delegation_results: Dict[str, Any]) -> Dict[str, Any]:
        """
        Entrega el reporte finalizado al Capitán General Contable.
        """
        print("CAPITÁN REPORTES CONTABLES: Preparando entrega de reporte final...")

        report = {
            "captain": self.__class__.__name__,
            "order_id": self.context.get('current_order', {}).get('id', 'N/A'),
            "status": "SUCCESS",
            "result": {
                "message": "Reporte generado exitosamente.",
                "report_location": f"/path/to/generated_report_{self.context.get('current_order', {}).get('details', {}).get('report_type')}.pdf" # Simulado
            }
        }

        print("CAPITÁN REPORTES CONTABLES: Reporte listo para entrega.")
        return report
