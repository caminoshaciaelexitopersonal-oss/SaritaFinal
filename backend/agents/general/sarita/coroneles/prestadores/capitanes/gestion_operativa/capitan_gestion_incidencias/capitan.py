from typing import Dict, Any

class CapitanGestionIncidencias:
    """
    Misión: Gestionar el ciclo de vida de las incidencias operativas, desde
    la detección hasta la resolución y el análisis post-mortem, minimizando
    el impacto en el cliente y la operación.
    """

    def __init__(self, coronel):
        self.coronel = coronel
        self.context = {}
        print(f"CAPITÁN GESTIÓN DE INCIDENCIAS: Inicializado.")

    def handle_order(self, order: Dict[str, Any]) -> Dict[str, Any]:
        """
        Recibe una orden del Coronel para gestionar una nueva incidencia.
        """
        print(f"CAPITÁN GESTIÓN DE INCIDENCIAS: Orden recibida - {order['type']}")
        self.context['current_order'] = order

        # THINK
        plan = self._create_plan()

        # DECIDE
        decision = self._make_decision(plan)

        # DELEGATE
        delegation_results = self._delegate_tasks(decision)

        report = self._generate_report(delegation_results)
        return report

    def _create_plan(self) -> Dict[str, Any]:
        """
        (THINK) Crea un plan de acción para la incidencia.
        """
        print("CAPITÁN GESTIÓN DE INCIDENCIAS: Creando plan de resolución...")
        incident_type = self.context.get('current_order', {}).get('details', {}).get('type')

        planned_steps = {
            "step_1": "clasificar_severidad_y_urgencia",
            "step_2": f"asignar_protocolo_de_respuesta_para_{incident_type}",
            "step_3": "identificar_tenientes_necesarios_para_resolucion"
        }
        return planned_steps

    def _make_decision(self, plan: Dict[str, Any]) -> Dict[str, Any]:
        """
        (DECIDE) Aprueba el plan y lo convierte en tareas delegables.
        """
        print("CAPITÁN GESTIÓN DE INCIDENCIAS: Tomando decisiones...")
        # En el futuro, aquí podría haber lógica de aprobación o modificación del plan.
        return plan # Por ahora, la decisión es ejecutar el plan tal cual.

    def _delegate_tasks(self, tasks: Dict[str, Any]) -> Dict[str, Any]:
        """
        (DELEGATE) Asigna las tareas a los futuros tenientes.
        """
        print("CAPITÁN GESTIÓN DE INCIDENCIAS: Delegando tareas a tenientes...")
        results = {}
        for step, task_description in tasks.items():
            # Simulación de la llamada a un teniente
            print(f"  - Delegando tarea: {task_description}")
            results[step] = {"status": "DELEGATED", "result": f"Tarea '{task_description}' delegada."}
        return results

    def _generate_report(self, delegation_results: Dict[str, Any]) -> Dict[str, Any]:
        """
        Prepara el informe de estado para el Coronel.
        """
        print("CAPITÁN GESTIÓN DE INCIDENCIAS: Preparando informe...")
        return {
            "captain": self.__class__.__name__,
            "status": "IN_PROGRESS",
            "summary": "Plan de resolución de incidencia en ejecución."
        }
