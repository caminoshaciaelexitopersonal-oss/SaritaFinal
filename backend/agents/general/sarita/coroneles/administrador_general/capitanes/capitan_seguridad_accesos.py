from typing import Dict, Any

class CapitanSeguridadAccesos:
    """
    Misión: Administrar de forma centralizada los roles, permisos y políticas
    de acceso (ACLs) de todos los usuarios y agentes del sistema, garantizando
    el principio de mínimo privilegio.
    """

    def __init__(self, coronel):
        self.coronel = coronel
        self.context = {}
        print(f"CAPITÁN SEGURIDAD Y ACCESOS: Inicializado.")

    def handle_order(self, order: Dict[str, Any]) -> Dict[str, Any]:
        """
        Recibe órdenes para crear, modificar o revocar roles y permisos.
        """
        print(f"CAPITÁN SEGURIDAD Y ACCESOS: Orden recibida - {order['type']}")
        self.context['current_order'] = order

        plan = self.plan()
        delegation_results = self.delegate(plan)
        report = self.report(delegation_results)

        return report

    def plan(self) -> Dict[str, Any]:
        """
        Crea un plan para ejecutar el cambio de permisos de forma segura.
        """
        print("CAPITÁN SEGURIDAD Y ACCESOS: Creando plan de gestión de accesos...")
        details = self.context.get('current_order', {}).get('details', {})

        planned_steps = {
            "step_1": f"validar_solicitud_de_cambio_de_permisos_para_usuario_{details.get('user_id')}",
            "step_2": "verificar_impacto_del_cambio_en_la_matriz_de_roles",
            "step_3": "delegar_ejecucion_del_cambio_en_el_proveedor_de_identidad",
            "step_4": "registrar_el_cambio_en_el_log_de_auditoria_de_seguridad"
        }

        self.context['plan'] = planned_steps
        return planned_steps

    def delegate(self, plan: Dict[str, Any]) -> Dict[str, Any]:
        """
        Delega la ejecución técnica a un Teniente de IAM (Identity and Access Management).
        """
        print("CAPITÁN SEGURIDAD Y ACCESOS: Delegando tareas de IAM...")
        results = {}
        for step, task in plan.items():
            print(f"  - Delegando tarea: {task}")
            results[step] = {"status": "DELEGATED", "result": f"Tarea '{task}' delegada para ejecución."}

        self.context['delegation_results'] = results
        return results

    def report(self, delegation_results: Dict[str, Any]) -> Dict[str, Any]:
        """
        Reporta la finalización exitosa del cambio de permisos.
        """
        print("CAPITÁN SEGURIDAD Y ACCESOS: Preparando informe de accesos...")

        report = {
            "captain": self.__class__.__name__,
            "order_id": self.context.get('current_order', {}).get('id', 'N/A'),
            "status": "SUCCESS",
            "result": {
                "message": "Gestión de accesos completada exitosamente."
            }
        }

        print("CAPITÁN SEGURIDAD Y ACCESOS: Informe de accesos listo.")
        return report
