from typing import Dict, Any

class CapitanBusquedaServicios:
    """
    Misión: Ejecutar búsquedas de servicios turísticos (vuelos, hoteles, actividades)
    basado en los criterios del turista, presentando resultados relevantes y filtrados.
    """

    def __init__(self, coronel):
        self.coronel = coronel
        self.context = {}
        print(f"CAPITÁN BÚSQUEDA DE SERVICIOS: Inicializado.")

    def handle_order(self, order: Dict[str, Any]) -> Dict[str, Any]:
        """
        Recibe una orden de búsqueda con parámetros específicos.
        """
        print(f"CAPITÁN BÚSQUEDA DE SERVICIOS: Orden recibida - {order['type']}")
        self.context['current_order'] = order

        plan = self.plan()
        delegation_results = self.delegate(plan)
        report = self.report(delegation_results)

        return report

    def plan(self) -> Dict[str, Any]:
        """
        Crea un plan para ejecutar la búsqueda en diferentes proveedores o sistemas.
        """
        print("CAPITÁN BÚSQUEDA DE SERVICIOS: Creando plan de búsqueda...")
        criteria = self.context.get('current_order', {}).get('details', {}).get('criteria')

        planned_steps = {
            "step_1": f"parsear_criterios_de_busqueda_'{criteria}'",
            "step_2": "delegar_consulta_a_tenientes_de_proveedores_hoteles",
            "step_3": "delegar_consulta_a_tenientes_de_proveedores_tours",
            "step_4": "consolidar_y_filtrar_resultados"
        }

        self.context['plan'] = planned_steps
        return planned_steps

    def delegate(self, plan: Dict[str, Any]) -> Dict[str, Any]:
        """
        Delega las consultas a los Tenientes que se integran con las APIs de proveedores.
        """
        print("CAPITÁN BÚSQUEDA DE SERVICIOS: Delegando consultas a Tenientes de proveedores...")
        results = {}
        for step, task in plan.items():
            print(f"  - Delegando tarea: {task}")
            results[step] = {"status": "DELEGATED", "result": f"Tarea '{task}' delegada para ejecución."}

        self.context['delegation_results'] = results
        return results

    def report(self, delegation_results: Dict[str, Any]) -> Dict[str, Any]:
        """
        Reporta los resultados de la búsqueda al Capitán de Experiencia.
        """
        print("CAPITÁN BÚSQUEDA DE SERVICIOS: Preparando informe de resultados de búsqueda...")

        report = {
            "captain": self.__class__.__name__,
            "order_id": self.context.get('current_order', {}).get('id', 'N/A'),
            "status": "SUCCESS",
            "result": {
                "message": "Búsqueda completada.",
                "match_count": 15, # Simulado
                "top_result": "Hotel El Mirador del Llano" # Simulado
            }
        }

        print("CAPITÁN BÚSQUEDA DE SERVICIOS: Informe de búsqueda listo.")
        return report
