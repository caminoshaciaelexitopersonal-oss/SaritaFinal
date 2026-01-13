from typing import Dict, Any

class CapitanEventosLocales:
    """
    Misión: Gestionar el calendario de eventos del municipio, coordinando la
    logística, promoción y ejecución de festivales, ferias y otras actividades
    de interés turístico.
    """

    def __init__(self, coronel):
        self.coronel = coronel
        self.context = {}
        print(f"CAPITÁN EVENTOS LOCALES: Inicializado.")

    def handle_order(self, order: Dict[str, Any]) -> Dict[str, Any]:
        """
        Recibe órdenes para crear, actualizar o promocionar un evento local.
        """
        print(f"CAPITÁN EVENTOS LOCALES: Orden recibida - {order['type']}")
        self.context['current_order'] = order

        plan = self.plan()
        delegation_results = self.delegate(plan)
        report = self.report(delegation_results)

        return report

    def plan(self) -> Dict[str, Any]:
        """
        Crea un plan de gestión para el evento.
        """
        print("CAPITÁN EVENTOS LOCALES: Creando plan de gestión de evento...")
        event_name = self.context.get('current_order', {}).get('details', {}).get('name')

        planned_steps = {
            "step_1": f"definir_cronograma_y_requerimientos_logisticos_para_{event_name}",
            "step_2": "delegar_plan_de_promocion_a_teniente_de_marketing_local",
            "step_3": "coordinar_permisos_y_seguridad_con_otras_entidades_municipales",
            "step_4": "establecer_metricas_de_exito_del_evento"
        }

        self.context['plan'] = planned_steps
        return planned_steps

    def delegate(self, plan: Dict[str, Any]) -> Dict[str, Any]:
        """
        Delega tareas de promoción y logística a Tenientes especialistas.
        """
        print("CAPITÁN EVENTOS LOCALES: Delegando tareas de gestión de evento...")
        results = {}
        for step, task in plan.items():
            print(f"  - Delegando tarea: {task}")
            results[step] = {"status": "DELEGATED", "result": f"Tarea '{task}' delegada para ejecución."}

        self.context['delegation_results'] = results
        return results

    def report(self, delegation_results: Dict[str, Any]) -> Dict[str, Any]:
        """
        Reporta el estado de la planificación del evento al Coronel Municipal.
        """
        print("CAPITÁN EVENTOS LOCALES: Preparando informe de evento...")

        report = {
            "captain": self.__class__.__name__,
            "order_id": self.context.get('current_order', {}).get('id', 'N/A'),
            "status": "IN_PROGRESS",
            "result": {
                "message": "Planificación del evento en marcha.",
                "event_status": "Logística definida, promoción en preparación." # Simulado
            }
        }

        print("CAPITÁN EVENTOS LOCALES: Informe de evento listo.")
        return report
