from typing import Dict, Any

class CapitanVentas:
    """
    Misión: Gestionar el proceso de cierre de ventas, desde la cotización
    hasta la facturación, asegurando el cumplimiento de los objetivos de ingresos.
    """

    def __init__(self, coronel):
        self.coronel = coronel
        self.context = {}
        print(f"CAPITÁN VENTAS: Inicializado.")

    def handle_order(self, order: Dict[str, Any]) -> Dict[str, Any]:
        """
        Recibe una orden para procesar una venta o un lote de prospectos calificados.
        """
        print(f"CAPITÁN VENTAS: Orden recibida - {order['type']}")
        self.context['current_order'] = order

        plan = self.plan()
        delegation_results = self.delegate(plan)
        report = self.report(delegation_results)

        return report

    def plan(self) -> Dict[str, Any]:
        """
        Crea un plan de acción para convertir un prospecto en cliente.
        """
        print("CAPITÁN VENTAS: Creando plan de cierre de venta...")
        prospect_id = self.context.get('current_order', {}).get('details', {}).get('prospect_id')

        planned_steps = {
            "step_1": f"asignar_teniente_de_ventas_a_prospecto_{prospect_id}",
            "step_2": "generar_cotizacion_personalizada",
            "step_3": "realizar_seguimiento_y_negociacion",
            "step_4": "procesar_cierre_y_facturacion"
        }

        self.context['plan'] = planned_steps
        return planned_steps

    def delegate(self, plan: Dict[str, Any]) -> Dict[str, Any]:
        """
        Delega las tareas del ciclo de venta a los Tenientes de ventas.
        """
        print("CAPITÁN VENTAS: Delegando tareas a Tenientes de Ventas...")
        results = {}
        for step, task in plan.items():
            print(f"  - Delegando tarea: {task}")
            results[step] = {"status": "DELEGATED", "result": f"Tarea '{task}' delegada exitosamente."}

        self.context['delegation_results'] = results
        return results

    def report(self, delegation_results: Dict[str, Any]) -> Dict[str, Any]:
        """
        Reporta el resultado de la venta (éxito o fracaso) al Capitán General Comercial.
        """
        print("CAPITÁN VENTAS: Preparando informe de resultados de venta...")

        report = {
            "captain": self.__class__.__name__,
            "order_id": self.context.get('current_order', {}).get('id', 'N/A'),
            "status": "SUCCESS",
            "result": {
                "message": "Venta cerrada exitosamente.",
                "prospect_id": self.context.get('current_order', {}).get('details', {}).get('prospect_id')
            }
        }

        print("CAPITÁN VENTAS: Informe de venta listo.")
        return report
