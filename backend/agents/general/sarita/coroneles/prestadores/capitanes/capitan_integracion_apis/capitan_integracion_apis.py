from typing import Dict, Any

class CapitanIntegracionApis:
    """
    Misión: Abstraer la complejidad de interactuar con las APIs de plataformas
    externas, proveyendo una interfaz unificada para que otros agentes
    puedan solicitar acciones sin conocer los detalles de cada API.
    """

    def __init__(self, coronel):
        self.coronel = coronel
        self.context = {}
        print(f"CAPITÁN INTEGRACIÓN APIS: Inicializado.")

    def handle_order(self, order: Dict[str, Any]) -> Dict[str, Any]:
        """
        Recibe órdenes genéricas como 'publicar_contenido_en_plataforma'.
        """
        print(f"CAPITÁN INTEGRACIÓN APIS: Orden recibida - {order['type']}")
        self.context['current_order'] = order

        plan = self.plan()
        delegation_results = self.delegate(plan)
        report = self.report(delegation_results)

        return report

    def plan(self) -> Dict[str, Any]:
        """
        Crea un plan para traducir la orden genérica a una llamada de API específica.
        """
        print("CAPITÁN INTEGRACIÓN APIS: Creando plan de ejecución de API...")
        details = self.context.get('current_order', {}).get('details', {})
        plataforma = details.get('plataforma')
        accion = details.get('accion')

        planned_steps = {
            "step_1": {"teniente": f"api_{plataforma}", "task": f"{accion}"}
        }

        self.context['plan'] = planned_steps
        return planned_steps

    def delegate(self, plan: Dict[str, Any]) -> Dict[str, Any]:
        """
        Delega la llamada de API al teniente especialista de esa plataforma.
        """
        print("CAPITÁN INTEGRACIÓN APIS: Delegando llamada de API...")
        results = {}
        for step, details in plan.items():
            print(f"  - Delegando tarea '{details['task']}' a Teniente '{details['teniente']}'")
            results[step] = {"status": "DELEGATED", "result": "Llamada a API simulada completada."}

        self.context['delegation_results'] = results
        return results

    def report(self, delegation_results: Dict[str, Any]) -> Dict[str, Any]:
        """
        Reporta el resultado de la interacción con la API.
        """
        print("CAPITÁN INTEGRACIÓN APIS: Preparando informe de API...")

        report = {
            "captain": self.__class__.__name__,
            "order_id": self.context.get('current_order', {}).get('id', 'N/A'),
            "status": "SUCCESS",
            "summary": "Interacción con API externa completada."
        }

        print("CAPITÁN INTEGRACIÓN APIS: Informe listo.")
        return report
