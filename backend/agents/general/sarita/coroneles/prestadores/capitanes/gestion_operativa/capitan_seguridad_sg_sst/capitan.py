from typing import Dict, Any

class CapitanSeguridadSGSST:
    """
    Misión: Gestionar y supervisar el Sistema de Gestión de Seguridad y Salud
    en el Trabajo (SG-SST), asegurando el cumplimiento normativo, la gestión
    de riesgos operativos y la respuesta a incidentes laborales.
    """

    def __init__(self, coronel):
        self.coronel = coronel
        self.context = {}
        print(f"CAPITÁN SEGURIDAD SG-SST: Inicializado.")

    def handle_order(self, order: Dict[str, Any]) -> Dict[str, Any]:
        """
        Recibe órdenes para realizar auditorías de seguridad o gestionar un incidente.
        """
        print(f"CAPITÁN SEGURIDAD SG-SST: Orden recibida - {order['type']}")
        self.context['current_order'] = order

        # THINK -> DECIDE -> DELEGATE
        plan = self._create_plan()
        decision = self._make_decision(plan)
        delegation_results = self._delegate_tasks(decision)

        report = self._generate_report(delegation_results)
        return report

    def _create_plan(self) -> Dict[str, Any]:
        """
        (THINK) Crea un plan de acción para la orden de seguridad.
        """
        print("CAPITÁN SEGURIDAD SG-SST: Creando plan de acción...")
        order_type = self.context.get('current_order', {}).get('type')

        planned_steps = {}
        if order_type == "realizar_inspeccion_de_riesgos":
            details = self.context.get('current_order', {}).get('details', {})
            planned_steps = {
                "step_1": f"revisar_matriz_de_riesgos_para_area_{details.get('area')}",
                "step_2": "delegar_inspeccion_en_sitio_a_teniente_de_seguridad",
                "step_3": "documentar_hallazgos_y_potenciales_no_conformidades"
            }

        return planned_steps

    def _make_decision(self, plan: Dict[str, Any]) -> Dict[str, Any]:
        """
        (DECIDE) Aprueba el plan de inspección.
        """
        print("CAPITÁN SEGURIDAD SG-SST: Tomando decisiones...")
        return plan

    def _delegate_tasks(self, tasks: Dict[str, Any]) -> Dict[str, Any]:
        """
        (DELEGATE) Asigna las tareas de inspección a los futuros tenientes.
        """
        print("CAPITÁN SEGURIDAD SG-SST: Delegando tareas de inspección...")
        results = {}
        for step, task_description in tasks.items():
            print(f"  - Delegando tarea: {task_description}")
            results[step] = {"status": "DELEGATED", "result": f"Tarea '{task_description}' delegada."}
        return results

    def _generate_report(self, delegation_results: Dict[str, Any]) -> Dict[str, Any]:
        """
        Prepara el informe de seguridad para el Coronel.
        """
        print("CAPITÁN SEGURIDAD SG-SST: Preparando informe...")
        return {
            "captain": self.__class__.__name__,
            "status": "IN_PROGRESS",
            "summary": "Inspección de seguridad en ejecución."
        }
