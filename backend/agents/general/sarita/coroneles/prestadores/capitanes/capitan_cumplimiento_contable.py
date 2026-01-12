from typing import Dict, Any

class CapitanCumplimientoContable:
    """
    Misión: Asegurar que todos los registros y procesos contables cumplan con
    las normativas fiscales y contables vigentes.
    """

    def __init__(self, coronel):
        self.coronel = coronel
        self.context = {}
        print(f"CAPITÁN CUMPLIMIENTO CONTABLE: Inicializado.")

    def handle_order(self, order: Dict[str, Any]) -> Dict[str, Any]:
        """
        Recibe una orden para auditar un área o proceso contable.
        """
        print(f"CAPITÁN CUMPLIMIENTO CONTABLE: Orden recibida - {order['type']}")
        self.context['current_order'] = order

        plan = self.plan()
        delegation_results = self.delegate(plan)
        report = self.report(delegation_results)

        return report

    def plan(self) -> Dict[str, Any]:
        """
        Crea un plan de auditoría para verificar el cumplimiento.
        """
        print("CAPITÁN CUMPLIMIENTO CONTABLE: Creando plan de auditoría de cumplimiento...")
        area_to_audit = self.context.get('current_order', {}).get('details', {}).get('area')

        planned_steps = {
            "step_1": f"revisar_ultimas_normativas_aplicables_a_{area_to_audit}",
            "step_2": "seleccionar_muestra_de_transacciones_para_auditar",
            "step_3": "delegar_verificacion_de_registros_contra_normativa",
            "step_4": "documentar_hallazgos_y_no_conformidades"
        }

        self.context['plan'] = planned_steps
        return planned_steps

    def delegate(self, plan: Dict[str, Any]) -> Dict[str, Any]:
        """
        Delega la ejecución de la auditoría a Tenientes auditores.
        """
        print("CAPITÁN CUMPLIMIENTO CONTABLE: Delegando tareas de auditoría...")
        results = {}
        for step, task in plan.items():
            print(f"  - Delegando tarea: {task}")
            results[step] = {"status": "DELEGATED", "result": f"Tarea '{task}' delegada para ejecución."}

        self.context['delegation_results'] = results
        return results

    def report(self, delegation_results: Dict[str, Any]) -> Dict[str, Any]:
        """
        Reporta los resultados de la auditoría de cumplimiento al Capitán General Contable.
        """
        print("CAPITÁN CUMPLIMIENTO CONTABLE: Preparando informe de auditoría...")

        report = {
            "captain": self.__class__.__name__,
            "order_id": self.context.get('current_order', {}).get('id', 'N/A'),
            "status": "SUCCESS",
            "result": {
                "message": "Auditoría de cumplimiento completada.",
                "findings": "No se encontraron no conformidades mayores." # Simulado
            }
        }

        print("CAPITÁN CUMPLIMIENTO CONTABLE: Informe de auditoría listo.")
        return report
