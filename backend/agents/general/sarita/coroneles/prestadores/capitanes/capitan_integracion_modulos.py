from typing import Dict, Any

class CapitanIntegracionModulos:
    """
    Misión: Facilitar la comunicación y la ejecución de procesos que involucren
    a múltiples dominios (e.g., Comercial, Operativo, Contable), asegurando
    la consistencia de los datos y la correcta secuencia de las operaciones.
    """

    def __init__(self, coronel):
        self.coronel = coronel
        self.context = {}
        print(f"CAPITÁN INTEGRACIÓN DE MÓDULOS: Inicializado.")

    def handle_order(self, order: Dict[str, Any]) -> Dict[str, Any]:
        """
        Recibe órdenes de procesos de negocio complejos que cruzan dominios.
        """
        print(f"CAPITÁN INTEGRACIÓN DE MÓDULOS: Orden recibida - {order['type']}")
        self.context['current_order'] = order

        plan = self.plan()
        delegation_results = self.delegate(plan)
        report = self.report(delegation_results)

        return report

    def plan(self) -> Dict[str, Any]:
        """
        Crea un plan de orquestación cross-dominio.
        """
        print("CAPITÁN INTEGRACIÓN DE MÓDULOS: Creando plan de orquestación...")
        order_type = self.context.get('current_order', {}).get('type')

        planned_steps = {}
        if order_type == "procesar_venta_hasta_contabilizacion":
             planned_steps = {
                "step_1": "delegar_cierre_de_venta_a_CapitanVentas",
                "step_2": "esperar_confirmacion_y_delegar_provision_a_CapitanPlanificacionServicios",
                "step_3": "esperar_confirmacion_y_delegar_registro_contable_a_CapitanContabilidadGeneral"
            }

        self.context['plan'] = planned_steps
        return planned_steps

    def delegate(self, plan: Dict[str, Any]) -> Dict[str, Any]:
        """
        Delega secuencialmente las tareas a los Capitanes Generales de cada dominio.
        """
        print("CAPITÁN INTEGRACIÓN DE MÓDULOS: Delegando tareas cross-dominio...")
        results = {}
        for step, task in plan.items():
            print(f"  - Delegando tarea: {task}")
            # En una implementación real, esto sería un proceso secuencial o en paralelo
            # con manejo de estados y callbacks.
            results[step] = {"status": "DELEGATED_TO_CAPTAIN", "result": f"Tarea '{task}' delegada exitosamente."}

        self.context['delegation_results'] = results
        return results

    def report(self, delegation_results: Dict[str, Any]) -> Dict[str, Any]:
        """
        Reporta la finalización exitosa del proceso de negocio integrado.
        """
        print("CAPITÁN INTEGRACIÓN DE MÓDULOS: Preparando informe de proceso integrado...")

        report = {
            "captain": self.__class__.__name__,
            "order_id": self.context.get('current_order', {}).get('id', 'N/A'),
            "status": "SUCCESS",
            "summary": f"Proceso de negocio '{self.context.get('current_order', {}).get('type')}' completado exitosamente a través de {len(delegation_results)} dominios.",
            "details": delegation_results
        }

        print("CAPITÁN INTEGRACIÓN DE MÓDULOS: Informe de proceso listo.")
        return report
