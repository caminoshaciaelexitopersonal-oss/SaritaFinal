from typing import Dict, Any

class CapitanBusquedaDocumental:
    """
    Misión: Ejecutar búsquedas complejas y recuperar documentos del archivo
    digital de forma eficiente y segura, respetando los permisos de acceso.
    """

    def __init__(self, coronel):
        self.coronel = coronel
        self.context = {}
        print(f"CAPITÁN BÚSQUEDA DOCUMENTAL: Inicializado.")

    def handle_order(self, order: Dict[str, Any]) -> Dict[str, Any]:
        """
        Recibe una solicitud de búsqueda con criterios específicos.
        """
        print(f"CAPITÁN BÚSQUEDA DOCUMENTAL: Orden recibida - {order['type']}")
        self.context['current_order'] = order

        plan = self.plan()
        delegation_results = self.delegate(plan)
        report = self.report(delegation_results)

        return report

    def plan(self) -> Dict[str, Any]:
        """
        Crea un plan de búsqueda optimizado para los criterios dados.
        """
        print("CAPITÁN BÚSQUEDA DOCUMENTAL: Creando plan de búsqueda...")
        query = self.context.get('current_order', {}).get('details', {}).get('query')

        planned_steps = {
            "step_1": f"parsear_y_optimizar_query_de_busqueda_para_'{query}'",
            "step_2": "ejecutar_busqueda_indexada_en_archivo_digital",
            "step_3": "filtrar_resultados_segun_permisos_del_solicitante",
            "step_4": "preparar_paquete_de_resultados_para_entrega"
        }

        self.context['plan'] = planned_steps
        return planned_steps

    def delegate(self, plan: Dict[str, Any]) -> Dict[str, Any]:
        """
        Delega la ejecución técnica de la búsqueda a un Teniente de sistemas.
        """
        print("CAPITÁN BÚSQUEDA DOCUMENTAL: Delegando ejecución de búsqueda...")
        results = {}
        for step, task in plan.items():
            print(f"  - Delegando tarea: {task}")
            results[step] = {"status": "DELEGATED", "result": f"Tarea '{task}' delegada para ejecución."}

        self.context['delegation_results'] = results
        return results

    def report(self, delegation_results: Dict[str, Any]) -> Dict[str, Any]:
        """
        Entrega los resultados de la búsqueda al solicitante o al Capitán General.
        """
        print("CAPITÁN BÚSQUEDA DOCUMENTAL: Preparando informe de resultados...")

        report = {
            "captain": self.__class__.__name__,
            "order_id": self.context.get('current_order', {}).get('id', 'N/A'),
            "status": "SUCCESS",
            "result": {
                "message": "Búsqueda completada.",
                "match_count": 3, # Simulado
                "results_location": "/path/to/search_results_package.zip" # Simulado
            }
        }

        print("CAPITÁN BÚSQUEDA DOCUMENTAL: Informe de resultados listo.")
        return report
