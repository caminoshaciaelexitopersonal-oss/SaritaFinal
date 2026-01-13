from typing import Dict, Any

class CapitanExperienciaTurista:
    """
    Misión: Orquestar la experiencia integral del turista, actuando como el
    punto de entrada principal para este dominio y coordinando a los demás
    capitanes especialistas para ofrecer un servicio cohesivo y personalizado.
    """

    def __init__(self, coronel):
        self.coronel = coronel
        self.context = {}
        print(f"CAPITÁN EXPERIENCIA DEL TURISTA: Inicializado.")

    def handle_order(self, order: Dict[str, Any]) -> Dict[str, Any]:
        """
        Recibe órdenes de alto nivel relacionadas con el viaje de un turista.
        """
        print(f"CAPITÁN EXPERIENCIA DEL TURISTA: Orden recibida - {order['type']}")
        self.context['current_order'] = order

        plan = self.plan()
        delegation_results = self.delegate(plan)
        report = self.report(delegation_results)

        return report

    def plan(self) -> Dict[str, Any]:
        """
        Crea un plan de acción integral basado en la fase del viaje del turista.
        """
        print("CAPITÁN EXPERIENCIA DEL TURISTA: Creando plan de experiencia...")
        order_type = self.context.get('current_order', {}).get('type')

        planned_steps = {}
        if order_type == "iniciar_planificacion_viaje":
            planned_steps = {
                "step_1": "delegar_busqueda_inicial_a_CapitanBusquedaServicios",
                "step_2": "delegar_actualizacion_de_contexto_a_CapitanContextoViaje",
                "step_3": "delegar_verificacion_de_perfil_a_CapitanGestionPerfil"
            }

        self.context['plan'] = planned_steps
        return planned_steps

    def delegate(self, plan: Dict[str, Any]) -> Dict[str, Any]:
        """
        Delega tareas a los capitanes especialistas del dominio del turista.
        """
        print("CAPITÁN EXPERIENCIA DEL TURISTA: Delegando tareas a Capitanes especialistas...")
        results = {}
        for step, task in plan.items():
            print(f"  - Delegando tarea: {task}")
            results[step] = {"status": "DELEGATED_TO_CAPTAIN", "result": f"Tarea '{task}' delegada exitosamente."}

        self.context['delegation_results'] = results
        return results

    def report(self, delegation_results: Dict[str, Any]) -> Dict[str, Any]:
        """
        Reporta un resumen del estado del viaje o la experiencia del turista.
        """
        print("CAPITÁN EXPERIENCIA DEL TURISTA: Preparando informe de experiencia...")

        report = {
            "captain": self.__class__.__name__,
            "order_id": self.context.get('current_order', {}).get('id', 'N/A'),
            "status": "IN_PROGRESS",
            "summary": "Planificación de viaje iniciada.",
            "details": delegation_results
        }

        print("CAPITÁN EXPERIENCIA DEL TURISTA: Informe de experiencia listo.")
        return report
