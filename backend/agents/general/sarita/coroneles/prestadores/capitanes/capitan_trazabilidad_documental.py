from typing import Dict, Any

class CapitanTrazabilidadDocumental:
    """
    Misión: Implementar y supervisar sistemas que registren el ciclo de vida
    de cada documento, desde su creación hasta su archivo o destrucción.
    """

    def __init__(self, coronel):
        self.coronel = coronel
        self.context = {}
        print(f"CAPITÁN TRAZABILIDAD DOCUMENTAL: Inicializado.")

    def handle_order(self, order: Dict[str, Any]) -> Dict[str, Any]:
        """
        Recibe órdenes para auditar la trazabilidad de un documento o tipo de documento.
        """
        print(f"CAPITÁN TRAZABILIDAD DOCUMENTAL: Orden recibida - {order['type']}")
        self.context['current_order'] = order

        plan = self.plan()
        delegation_results = self.delegate(plan)
        report = self.report(delegation_results)

        return report

    def plan(self) -> Dict[str, Any]:
        """
        Crea un plan para verificar o implementar la trazabilidad.
        """
        print("CAPITÁN TRAZABILIDAD DOCUMENTAL: Creando plan de auditoría de trazabilidad...")
        document_type = self.context.get('current_order', {}).get('details', {}).get('doc_type')

        planned_steps = {
            "step_1": f"revisar_metadatos_de_versionado_para_{document_type}",
            "step_2": f"verificar_logs_de_acceso_y_modificacion_para_{document_type}",
            "step_3": "confirmar_consistencia_de_la_cadena_de_custodia_digital",
        }

        self.context['plan'] = planned_steps
        return planned_steps

    def delegate(self, plan: Dict[str, Any]) -> Dict[str, Any]:
        """
        Delega tareas de auditoría de logs y metadatos a Tenientes técnicos.
        """
        print("CAPITÁN TRAZABILIDAD DOCUMENTAL: Delegando tareas de auditoría técnica...")
        results = {}
        for step, task in plan.items():
            print(f"  - Delegando tarea: {task}")
            results[step] = {"status": "DELEGATED", "result": f"Tarea '{task}' delegada para ejecución."}

        self.context['delegation_results'] = results
        return results

    def report(self, delegation_results: Dict[str, Any]) -> Dict[str, Any]:
        """
        Reporta los resultados de la auditoría de trazabilidad.
        """
        print("CAPITÁN TRAZABILIDAD DOCUMENTAL: Preparando informe de trazabilidad...")

        report = {
            "captain": self.__class__.__name__,
            "order_id": self.context.get('current_order', {}).get('id', 'N/A'),
            "status": "SUCCESS",
            "result": {
                "message": "Auditoría de trazabilidad completada.",
                "findings": "Ciclo de vida del documento verificado y consistente." # Simulado
            }
        }

        print("CAPITÁN TRAZABILIDAD DOCUMENTAL: Informe de trazabilidad listo.")
        return report
