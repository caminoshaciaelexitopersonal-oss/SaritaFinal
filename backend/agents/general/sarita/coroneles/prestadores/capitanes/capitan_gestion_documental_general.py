from typing import Dict, Any

class CapitanGestionDocumentalGeneral:
    """
    Misión: Orquestar la estrategia de gestión documental de la empresa,
    asegurando la correcta clasificación, almacenamiento, trazabilidad y
    cumplimiento de las políticas de retención de todos los documentos.
    """

    def __init__(self, coronel):
        self.coronel = coronel
        self.context = {}
        print(f"CAPITÁN GESTIÓN DOCUMENTAL GENERAL: Inicializado.")

    def handle_order(self, order: Dict[str, Any]) -> Dict[str, Any]:
        """
        Recibe órdenes de alto nivel, como 'auditar cumplimiento de políticas'.
        """
        print(f"CAPITÁN GESTIÓN DOCUMENTAL GENERAL: Orden recibida - {order['type']}")
        self.context['current_order'] = order

        plan = self.plan()
        delegation_results = self.delegate(plan)
        report = self.report(delegation_results)

        return report

    def plan(self) -> Dict[str, Any]:
        """
        Crea un plan documental integrado para cumplir la orden.
        """
        print("CAPITÁN GESTIÓN DOCUMENTAL GENERAL: Creando plan documental...")
        order_type = self.context.get('current_order', {}).get('type')

        planned_steps = {}
        if order_type == "implementar_nueva_politica_archivistica":
            planned_steps = {
                "step_1": "delegar_actualizacion_de_esquemas_a_CapitanPoliticasRetencion",
                "step_2": "delegar_aplicacion_de_trazabilidad_a_CapitanTrazabilidadDocumental",
                "step_3": "delegar_comunicacion_y_entrenamiento_a_Tenientes"
            }

        self.context['plan'] = planned_steps
        return planned_steps

    def delegate(self, plan: Dict[str, Any]) -> Dict[str, Any]:
        """
        Delega tareas a los capitanes archivísticos especialistas.
        """
        print("CAPITÁN GESTIÓN DOCUMENTAL GENERAL: Delegando tareas a Capitanes Archivísticos...")
        results = {}
        for step, task in plan.items():
            print(f"  - Delegando tarea: {task}")
            results[step] = {"status": "DELEGATED_TO_CAPTAIN", "result": f"Tarea '{task}' delegada exitosamente."}

        self.context['delegation_results'] = results
        return results

    def report(self, delegation_results: Dict[str, Any]) -> Dict[str, Any]:
        """
        Reporta el estado de la gestión documental al Coronel.
        """
        print("CAPITÁN GESTIÓN DOCUMENTAL GENERAL: Preparando informe de estado documental...")

        report = {
            "captain": self.__class__.__name__,
            "order_id": self.context.get('current_order', {}).get('id', 'N/A'),
            "status": "SUCCESS",
            "summary": f"Proceso documental '{self.context.get('current_order', {}).get('type')}' completado.",
            "details": delegation_results
        }

        print("CAPITÁN GESTIÓN DOCUMENTAL GENERAL: Informe documental listo.")
        return report
