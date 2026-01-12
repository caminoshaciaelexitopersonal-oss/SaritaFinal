from typing import Dict, Any

class CapitanTurismoLocal:
    """
    Misión: Promocionar activamente los atractivos, servicios y la marca
    turística del municipio, gestionando el inventario turístico local y
    creando material de marketing.
    """

    def __init__(self, coronel):
        self.coronel = coronel
        self.context = {}
        print(f"CAPITÁN TURISMO LOCAL: Inicializado.")

    def handle_order(self, order: Dict[str, Any]) -> Dict[str, Any]:
        """
        Recibe órdenes para lanzar campañas de promoción o actualizar el inventario turístico.
        """
        print(f"CAPITÁN TURISMO LOCAL: Orden recibida - {order['type']}")
        self.context['current_order'] = order

        plan = self.plan()
        delegation_results = self.delegate(plan)
        report = self.report(delegation_results)

        return report

    def plan(self) -> Dict[str, Any]:
        """
        Crea un plan de promoción o de gestión de inventario.
        """
        print("CAPITÁN TURISMO LOCAL: Creando plan de acción...")
        order_type = self.context.get('current_order', {}).get('type')

        planned_steps = {}
        if order_type == "actualizar_inventario_turistico":
            planned_steps = {
                "step_1": "delegar_levantamiento_de_nuevos_atractivos_en_campo",
                "step_2": "validar_y_clasificar_informacion_recibida",
                "step_3": "actualizar_base_de_datos_de_inventario_turistico"
            }

        self.context['plan'] = planned_steps
        return planned_steps

    def delegate(self, plan: Dict[str, Any]) -> Dict[str, Any]:
        """
        Delega tareas de campo y de marketing a Tenientes locales.
        """
        print("CAPITÁN TURISMO LOCAL: Delegando tareas locales...")
        results = {}
        for step, task in plan.items():
            print(f"  - Delegando tarea: {task}")
            results[step] = {"status": "DELEGATED", "result": f"Tarea '{task}' delegada para ejecución."}

        self.context['delegation_results'] = results
        return results

    def report(self, delegation_results: Dict[str, Any]) -> Dict[str, Any]:
        """
        Reporta el estado de las actividades de promoción o la actualización del inventario.
        """
        print("CAPITÁN TURISMO LOCAL: Preparando informe de turismo local...")

        report = {
            "captain": self.__class__.__name__,
            "order_id": self.context.get('current_order', {}).get('id', 'N/A'),
            "status": "SUCCESS",
            "result": {
                "message": "Actualización de inventario turístico completada.",
                "new_entries": 5 # Simulado
            }
        }

        print("CAPITÁN TURISMO LOCAL: Informe listo.")
        return report
