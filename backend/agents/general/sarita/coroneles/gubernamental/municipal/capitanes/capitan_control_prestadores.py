from typing import Dict, Any

class CapitanControlPrestadores:
    """
    Misión: Supervisar y fiscalizar a los prestadores de servicios turísticos
    del municipio para asegurar que cumplan con la normativa local, los
    registros y los estándares de calidad definidos.
    """

    def __init__(self, coronel):
        self.coronel = coronel
        self.context = {}
        print(f"CAPITÁN CONTROL DE PRESTADORES: Inicializado.")

    def handle_order(self, order: Dict[str, Any]) -> Dict[str, Any]:
        """
        Recibe órdenes para realizar una inspección o auditoría de cumplimiento a un prestador.
        """
        print(f"CAPITÁN CONTROL DE PRESTADORES: Orden recibida - {order['type']}")
        self.context['current_order'] = order

        plan = self.plan()
        delegation_results = self.delegate(plan)
        report = self.report(delegation_results)

        return report

    def plan(self) -> Dict[str, Any]:
        """
        Crea un plan de inspección para el prestador.
        """
        print("CAPITÁN CONTROL DE PRESTADORES: Creando plan de inspección...")
        prestador_id = self.context.get('current_order', {}).get('details', {}).get('prestador_id')

        planned_steps = {
            "step_1": f"revisar_documentacion_y_permisos_vigentes_de_{prestador_id}",
            "step_2": "programar_y_delegar_visita_de_inspeccion_en_sitio",
            "step_3": "evaluar_informe_de_inspeccion_y_verificar_cumplimiento",
            "step_4": "emitir_concepto_de_cumplimiento_o_requerimiento"
        }

        self.context['plan'] = planned_steps
        return planned_steps

    def delegate(self, plan: Dict[str, Any]) -> Dict[str, Any]:
        """
        Delega la inspección en sitio a Tenientes inspectores.
        """
        print("CAPITÁN CONTROL DE PRESTADORES: Delegando tareas de inspección...")
        results = {}
        for step, task in plan.items():
            print(f"  - Delegando tarea: {task}")
            results[step] = {"status": "DELEGATED", "result": f"Tarea '{task}' delegada para ejecución."}

        self.context['delegation_results'] = results
        return results

    def report(self, delegation_results: Dict[str, Any]) -> Dict[str, Any]:
        """
        Reporta el resultado de la inspección al Coronel Municipal.
        """
        print("CAPITÁN CONTROL DE PRESTADORES: Preparando informe de inspección...")

        report = {
            "captain": self.__class__.__name__,
            "order_id": self.context.get('current_order', {}).get('id', 'N/A'),
            "status": "SUCCESS",
            "result": {
                "message": "Inspección de prestador finalizada.",
                "outcome": "Cumple con la normativa vigente." # Simulado
            }
        }

        print("CAPITÁN CONTROL DE PRESTADORES: Informe de inspección listo.")
        return report
