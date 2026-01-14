from typing import Dict, Any

class CapitanGestionOperativaGeneral:
    """
    Misión: Orquesta y supervisa a todos los demás capitanes de Gestión Operativa,
    asegurando la cohesión y eficiencia del dominio. Es el punto de entrada principal
    para órdenes operativas complejas.
    """

    def __init__(self, coronel):
        self.coronel = coronel
        self.context = {}
        print(f"CAPITÁN GESTIÓN OPERATIVA GENERAL: Inicializado.")

    def handle_order(self, order: Dict[str, Any]) -> Dict[str, Any]:
        """
        Recibe una orden del Coronel, la procesa y gestiona su ejecución.
        """
        print(f"CAPITÁN GESTIÓN OPERATIVA GENERAL: Orden recibida - {order['type']}")
        self.context['current_order'] = order

        plan = self.plan()
        delegation_results = self.delegate(plan)
        report = self.report(delegation_results)

        return report

    def plan(self) -> Dict[str, Any]:
        """
        Crea un plan táctico para cumplir la orden recibida, coordinando a otros capitanes operativos.
        """
        print("CAPITÁN GESTIÓN OPERATIVA GENERAL: Creando plan táctico...")
        # Lógica para determinar qué otros capitanes operativos se necesitan
        # Por ejemplo, una orden de "lanzar nuevo tour" requeriría planificación y control.
        order_type = self.context.get('current_order', {}).get('type')

        planned_steps = {}
        if order_type == "gestionar_servicio_completo":
             planned_steps = {
                "step_1": "delegar_planificacion_a_CapitanPlanificacionServicios",
                "step_2": "delegar_supervision_a_CapitanControlOperativo",
                "step_3": "monitorear_incidentes_con_CapitanIncidentesOperativos"
            }

        self.context['plan'] = planned_steps
        return planned_steps

    def delegate(self, plan: Dict[str, Any]) -> Dict[str, Any]:
        """
        Delega la ejecución de los pasos del plan a los Capitanes Operativos específicos.
        """
        print("CAPITÁN GESTIÓN OPERATIVA GENERAL: Delegando tareas a otros Capitanes...")
        results = {}
        for step, task in plan.items():
            # En el futuro, se comunicaría con la instancia del Capitán correspondiente.
            print(f"  - Delegando tarea: {task}")
            results[step] = {"status": "DELEGATED_TO_CAPTAIN", "result": f"Tarea '{task}' delegada exitosamente."}

        self.context['delegation_results'] = results
        return results

    def report(self, delegation_results: Dict[str, Any]) -> Dict[str, Any]:
        """
        Reporta un resumen consolidado del estado de la operación al Coronel.
        """
        print("CAPITÁN GESTIÓN OPERATIVA GENERAL: Preparando informe consolidado para el Coronel...")

        final_status = "SUCCESS"
        for result in delegation_results.values():
            if result['status'] != "DELEGATED_TO_CAPTAIN":
                final_status = "FAILED"
                break

        report = {
            "captain": self.__class__.__name__,
            "order_id": self.context.get('current_order', {}).get('id', 'N/A'),
            "status": final_status,
            "summary": f"Operación completada con {len(delegation_results)} pasos delegados.",
            "details": delegation_results
        }

        print("CAPITÁN GESTIÓN OPERATIVA GENERAL: Informe final listo.")
        return report
