from typing import Dict, Any

class CapitanRutasTuristicas:
    """
    Misión: Diseñar, documentar y promocionar rutas turísticas que conecten
    múltiples municipios y atractivos dentro del departamento, creando productos
    turísticos cohesivos y atractivos.
    """

    def __init__(self, coronel):
        self.coronel = coronel
        self.context = {}
        print(f"CAPITÁN RUTAS TURÍSTICAS: Inicializado.")

    def handle_order(self, order: Dict[str, Any]) -> Dict[str, Any]:
        """
        Recibe órdenes para crear o actualizar una ruta turística.
        """
        print(f"CAPITÁN RUTAS TURÍSTICAS: Orden recibida - {order['type']}")
        self.context['current_order'] = order

        plan = self.plan()
        delegation_results = self.delegate(plan)
        report = self.report(delegation_results)

        return report

    def plan(self) -> Dict[str, Any]:
        """
        Crea un plan para el diseño de la ruta.
        """
        print("CAPITÁN RUTAS TURÍSTICAS: Creando plan de diseño de ruta...")
        route_name = self.context.get('current_order', {}).get('details', {}).get('name')

        planned_steps = {
            "step_1": f"investigar_y_mapear_atractivos_potenciales_para_{route_name}",
            "step_2": "definir_trazado_de_la_ruta_y_puntos_de_interes",
            "step_3": "delegar_levantamiento_de_inventario_de_prestadores_en_ruta",
            "step_4": "diseñar_material_promocional_y_mapas"
        }

        self.context['plan'] = planned_steps
        return planned_steps

    def delegate(self, plan: Dict[str, Any]) -> Dict[str, Any]:
        """
        Delega tareas de levantamiento de información y diseño a Tenientes.
        """
        print("CAPITÁN RUTAS TURÍSTICAS: Delegando tareas de diseño...")
        results = {}
        for step, task in plan.items():
            print(f"  - Delegando tarea: {task}")
            results[step] = {"status": "DELEGATED", "result": f"Tarea '{task}' delegada para ejecución."}

        self.context['delegation_results'] = results
        return results

    def report(self, delegation_results: Dict[str, Any]) -> Dict[str, Any]:
        """
        Reporta la finalización del diseño de la ruta turística.
        """
        print("CAPITÁN RUTAS TURÍSTICAS: Preparando informe de ruta diseñada...")

        report = {
            "captain": self.__class__.__name__,
            "order_id": self.context.get('current_order', {}).get('id', 'N/A'),
            "status": "SUCCESS",
            "result": {
                "message": "Ruta turística diseñada y lista para promoción.",
                "route_name": self.context.get('current_order', {}).get('details', {}).get('name')
            }
        }

        print("CAPITÁN RUTAS TURÍSTICAS: Informe de ruta listo.")
        return report
