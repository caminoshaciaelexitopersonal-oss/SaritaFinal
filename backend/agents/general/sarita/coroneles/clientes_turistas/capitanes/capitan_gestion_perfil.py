from typing import Dict, Any

class CapitanGestionPerfil:
    """
    Misión: Administrar los datos del perfil del turista, incluyendo
    información personal, preferencias de viaje, historial y documentos.
    """

    def __init__(self, coronel):
        self.coronel = coronel
        self.context = {}
        print(f"CAPITÁN GESTIÓN DE PERFIL: Inicializado.")

    def handle_order(self, order: Dict[str, Any]) -> Dict[str, Any]:
        """
        Recibe órdenes para leer o actualizar datos del perfil de un usuario.
        """
        print(f"CAPITÁN GESTIÓN DE PERFIL: Orden recibida - {order['type']}")
        self.context['current_order'] = order

        plan = self.plan()
        delegation_results = self.delegate(plan)
        report = self.report(delegation_results)

        return report

    def plan(self) -> Dict[str, Any]:
        """
        Crea un plan para la acción solicitada sobre el perfil.
        """
        print("CAPITÁN GESTIÓN DE PERFIL: Creando plan de gestión de perfil...")
        order_type = self.context.get('current_order', {}).get('type')

        planned_steps = {}
        if order_type == "actualizar_preferencias":
            planned_steps = {
                "step_1": "validar_nuevas_preferencias",
                "step_2": "delegar_escritura_segura_en_base_de_datos_de_perfiles",
                "step_3": "confirmar_actualizacion_y_refrescar_contexto"
            }

        self.context['plan'] = planned_steps
        return planned_steps

    def delegate(self, plan: Dict[str, Any]) -> Dict[str, Any]:
        """
        Delega la interacción con la base de datos a un Teniente de persistencia.
        """
        print("CAPITÁN GESTIÓN DE PERFIL: Delegando tareas de base de datos...")
        results = {}
        for step, task in plan.items():
            print(f"  - Delegando tarea: {task}")
            results[step] = {"status": "DELEGATED", "result": f"Tarea '{task}' delegada para ejecución."}

        self.context['delegation_results'] = results
        return results

    def report(self, delegation_results: Dict[str, Any]) -> Dict[str, Any]:
        """
        Reporta el éxito de la operación sobre el perfil.
        """
        print("CAPITÁN GESTIÓN DE PERFIL: Preparando informe de actualización...")

        report = {
            "captain": self.__class__.__name__,
            "order_id": self.context.get('current_order', {}).get('id', 'N/A'),
            "status": "SUCCESS",
            "result": {
                "message": "Perfil de usuario actualizado exitosamente."
            }
        }

        print("CAPITÁN GESTIÓN DE PERFIL: Informe de actualización listo.")
        return report
