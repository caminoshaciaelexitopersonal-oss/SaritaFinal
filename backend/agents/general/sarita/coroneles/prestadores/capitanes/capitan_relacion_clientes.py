from typing import Dict, Any

class CapitanRelacionClientes:
    """
    Misión: Gestionar el ciclo de vida del cliente post-venta, enfocándose en la
    fidelización, satisfacción y resolución de problemas (CRM).
    """

    def __init__(self, coronel):
        self.coronel = coronel
        self.context = {}
        print(f"CAPITÁN RELACIÓN CON CLIENTES: Inicializado.")

    def handle_order(self, order: Dict[str, Any]) -> Dict[str, Any]:
        """
        Recibe órdenes para gestionar la relación con un cliente o segmento de clientes.
        """
        print(f"CAPITÁN RELACIÓN CON CLIENTES: Orden recibida - {order['type']}")
        self.context['current_order'] = order

        plan = self.plan()
        delegation_results = self.delegate(plan)
        report = self.report(delegation_results)

        return report

    def plan(self) -> Dict[str, Any]:
        """
        Crea un plan de acción para mejorar la relación con el cliente.
        """
        print("CAPITÁN RELACIÓN CON CLIENTES: Creando plan de fidelización...")
        customer_id = self.context.get('current_order', {}).get('details', {}).get('customer_id')

        planned_steps = {
            "step_1": f"analizar_historial_de_interacciones_de_{customer_id}",
            "step_2": "identificar_oportunidades_de_upselling_o_mejora",
            "step_3": "programar_comunicacion_de_seguimiento_personalizada",
            "step_4": "recopilar_feedback_de_satisfaccion"
        }

        self.context['plan'] = planned_steps
        return planned_steps

    def delegate(self, plan: Dict[str, Any]) -> Dict[str, Any]:
        """
        Delega tareas a Tenientes de CRM o soporte al cliente.
        """
        print("CAPITÁN RELACIÓN CON CLIENTES: Delegando tareas de CRM...")
        results = {}
        for step, task in plan.items():
            print(f"  - Delegando tarea: {task}")
            results[step] = {"status": "DELEGATED", "result": f"Tarea '{task}' delegada para ejecución."}

        self.context['delegation_results'] = results
        return results

    def report(self, delegation_results: Dict[str, Any]) -> Dict[str, Any]:
        """
        Reporta el estado de la relación con el cliente y los KPIs de satisfacción.
        """
        print("CAPITÁN RELACIÓN CON CLIENTES: Preparando informe de cliente...")

        report = {
            "captain": self.__class__.__name__,
            "order_id": self.context.get('current_order', {}).get('id', 'N/A'),
            "status": "SUCCESS",
            "result": {
                "message": "Plan de relación con cliente ejecutado.",
                "customer_satisfaction_index": "95%" # Valor simulado
            }
        }

        print("CAPITÁN RELACIÓN CON CLIENTES: Informe de cliente listo.")
        return report
