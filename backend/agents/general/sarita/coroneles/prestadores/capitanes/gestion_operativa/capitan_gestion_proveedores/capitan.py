from typing import Dict, Any

class CapitanGestionProveedores:
    """
    Misión: Gestionar la relación con proveedores operativos externos
    (guías, transportistas, operadores aliados), asegurando su disponibilidad,
    calidad y cumplimiento de acuerdos.
    """

    def __init__(self, coronel):
        self.coronel = coronel
        self.context = {}
        print(f"CAPITÁN GESTIÓN DE PROVEEDORES: Inicializado.")

    def handle_order(self, order: Dict[str, Any]) -> Dict[str, Any]:
        """
        Recibe órdenes para buscar, asignar o evaluar un proveedor.
        """
        print(f"CAPITÁN GESTIÓN DE PROVEEDORES: Orden recibida - {order['type']}")
        self.context['current_order'] = order

        # THINK -> DECIDE -> DELEGATE
        plan = self._create_plan()
        decision = self._make_decision(plan)
        delegation_results = self._delegate_tasks(decision)

        report = self._generate_report(delegation_results)
        return report

    def _create_plan(self) -> Dict[str, Any]:
        """
        (THINK) Crea un plan para la gestión del proveedor.
        """
        print("CAPITÁN GESTIÓN DE PROVEEDORES: Creando plan de gestión...")
        order_type = self.context.get('current_order', {}).get('type')

        planned_steps = {}
        if order_type == "asignar_proveedor_a_servicio":
            details = self.context.get('current_order', {}).get('details', {})
            planned_steps = {
                "step_1": f"buscar_proveedores_disponibles_para_fecha_{details.get('fecha')}",
                "step_2": f"validar_cumplimiento_y_calificacion_de_candidatos",
                "step_3": "delegar_asignacion_y_confirmacion_a_teniente_de_logistica"
            }

        return planned_steps

    def _make_decision(self, plan: Dict[str, Any]) -> Dict[str, Any]:
        """
        (DECIDE) Aprueba el plan de asignación.
        """
        print("CAPITÁN GESTIÓN DE PROVEEDORES: Tomando decisiones...")
        return plan

    def _delegate_tasks(self, tasks: Dict[str, Any]) -> Dict[str, Any]:
        """
        (DELEGATE) Asigna las tareas de logística a los futuros tenientes.
        """
        print("CAPITÁN GESTIÓN DE PROVEEDORES: Delegando tareas de asignación...")
        results = {}
        for step, task_description in tasks.items():
            print(f"  - Delegando tarea: {task_description}")
            results[step] = {"status": "DELEGATED", "result": f"Tarea '{task_description}' delegada."}
        return results

    def _generate_report(self, delegation_results: Dict[str, Any]) -> Dict[str, Any]:
        """
        Prepara el informe de gestión de proveedores.
        """
        print("CAPITÁN GESTIÓN DE PROVEEDORES: Preparando informe...")
        return {
            "captain": self.__class__.__name__,
            "status": "SUCCESS",
            "summary": "Proveedor asignado exitosamente."
        }
