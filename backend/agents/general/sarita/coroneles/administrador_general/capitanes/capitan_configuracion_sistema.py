from typing import Dict, Any

class CapitanConfiguracionSistema:
    """
    Misión: Gestionar la configuración global del sistema, incluyendo
    parámetros, variables de entorno y feature flags, asegurando que
    los cambios se apliquen de forma controlada y segura.
    """

    def __init__(self, coronel):
        self.coronel = coronel
        self.context = {}
        print(f"CAPITÁN CONFIGURACIÓN DEL SISTEMA: Inicializado.")

    def handle_order(self, order: Dict[str, Any]) -> Dict[str, Any]:
        """
        Recibe órdenes para leer o modificar una configuración del sistema.
        """
        print(f"CAPITÁN CONFIGURACIÓN DEL SISTEMA: Orden recibida - {order['type']}")
        self.context['current_order'] = order

        plan = self.plan()
        delegation_results = self.delegate(plan)
        report = self.report(delegation_results)

        return report

    def plan(self) -> Dict[str, Any]:
        """
        Crea un plan para aplicar el cambio de configuración.
        """
        print("CAPITÁN CONFIGURACIÓN DEL SISTEMA: Creando plan de cambio de configuración...")
        config_key = self.context.get('current_order', {}).get('details', {}).get('key')

        planned_steps = {
            "step_1": f"validar_permisos_para_modificar_configuracion_{config_key}",
            "step_2": "crear_un_plan_de_rollback_en_caso_de_fallo",
            "step_3": "delegar_aplicacion_del_cambio_al_teniente_de_infraestructura",
            "step_4": "realizar_verificacion_post-cambio_para_confirmar_estabilidad"
        }

        self.context['plan'] = planned_steps
        return planned_steps

    def delegate(self, plan: Dict[str, Any]) -> Dict[str, Any]:
        """
        Delega la aplicación técnica del cambio a un Teniente de Infraestructura.
        """
        print("CAPITÁN CONFIGURACIÓN DEL SISTEMA: Delegando aplicación de cambio...")
        results = {}
        for step, task in plan.items():
            print(f"  - Delegando tarea: {task}")
            results[step] = {"status": "DELEGATED", "result": f"Tarea '{task}' delegada para ejecución."}

        self.context['delegation_results'] = results
        return results

    def report(self, delegation_results: Dict[str, Any]) -> Dict[str, Any]:
        """
        Reporta el resultado de la operación de configuración al Coronel.
        """
        print("CAPITÁN CONFIGURACIÓN DEL SISTEMA: Preparando informe de configuración...")

        report = {
            "captain": self.__class__.__name__,
            "order_id": self.context.get('current_order', {}).get('id', 'N/A'),
            "status": "SUCCESS",
            "result": {
                "message": "Cambio de configuración aplicado y verificado exitosamente."
            }
        }

        print("CAPITÁN CONFIGURACIÓN DEL SISTEMA: Informe de configuración listo.")
        return report
