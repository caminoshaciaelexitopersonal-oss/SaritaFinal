from typing import Dict, Any

class CapitanPoliticasRetencion:
    """
    Misión: Definir, implementar y hacer cumplir las políticas de retención
    documental, determinando cuánto tiempo debe conservarse cada tipo de documento.
    """

    def __init__(self, coronel):
        self.coronel = coronel
        self.context = {}
        print(f"CAPITÁN POLÍTICAS DE RETENCIÓN: Inicializado.")

    def handle_order(self, order: Dict[str, Any]) -> Dict[str, Any]:
        """
        Recibe órdenes para definir o actualizar una política de retención.
        """
        print(f"CAPITÁN POLÍTICAS DE RETENCIÓN: Orden recibida - {order['type']}")
        self.context['current_order'] = order

        plan = self.plan()
        delegation_results = self.delegate(plan)
        report = self.report(delegation_results)

        return report

    def plan(self) -> Dict[str, Any]:
        """
        Crea un plan para establecer o actualizar una política.
        """
        print("CAPITÁN POLÍTICAS DE RETENCIÓN: Creando plan de política de retención...")
        document_type = self.context.get('current_order', {}).get('details', {}).get('doc_type')

        planned_steps = {
            "step_1": f"investigar_requerimientos_legales_y_fiscales_para_{document_type}",
            "step_2": "definir_periodo_de_retencion_activo_y_pasivo",
            "step_3": "establecer_procedimiento_de_destruccion_segura",
            "step_4": "actualizar_matriz_de_retencion_documental"
        }

        self.context['plan'] = planned_steps
        return planned_steps

    def delegate(self, plan: Dict[str, Any]) -> Dict[str, Any]:
        """
        Delega tareas de investigación legal y actualización de sistemas a Tenientes.
        """
        print("CAPITÁN POLÍTICAS DE RETENCIÓN: Delegando tareas de definición de políticas...")
        results = {}
        for step, task in plan.items():
            print(f"  - Delegando tarea: {task}")
            results[step] = {"status": "DELEGATED", "result": f"Tarea '{task}' delegada para ejecución."}

        self.context['delegation_results'] = results
        return results

    def report(self, delegation_results: Dict[str, Any]) -> Dict[str, Any]:
        """
        Reporta la nueva política de retención definida al Capitán General.
        """
        print("CAPITÁN POLÍTICAS DE RETENCIÓN: Preparando informe de nueva política...")

        report = {
            "captain": self.__class__.__name__,
            "order_id": self.context.get('current_order', {}).get('id', 'N/A'),
            "status": "SUCCESS",
            "result": {
                "message": "Política de retención definida y actualizada.",
                "policy_summary": f"Documentos tipo '{self.context.get('current_order', {}).get('details', {}).get('doc_type')}' retener por 7 años." # Simulado
            }
        }

        print("CAPITÁN POLÍTICAS DE RETENCIÓN: Informe de política listo.")
        return report
