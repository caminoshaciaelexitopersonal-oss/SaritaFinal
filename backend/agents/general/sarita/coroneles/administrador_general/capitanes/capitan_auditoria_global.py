from typing import Dict, Any

class CapitanAuditoriaGlobal:
    """
    Misión: Ejecutar auditorías transversales y programadas sobre todos los
    dominios y procesos del sistema para identificar anomalías, brechas de
-   seguridad, ineficiencias o desviaciones de las políticas establecidas.
    """

    def __init__(self, coronel):
        self.coronel = coronel
        self.context = {}
        print(f"CAPITÁN AUDITORÍA GLOBAL: Inicializado.")

    def handle_order(self, order: Dict[str, Any]) -> Dict[str, Any]:
        """
        Recibe órdenes para iniciar una auditoría específica (e.g., 'auditar_procesos_de_facturacion').
        """
        print(f"CAPITÁN AUDITORÍA GLOBAL: Orden recibida - {order['type']}")
        self.context['current_order'] = order

        plan = self.plan()
        delegation_results = self.delegate(plan)
        report = self.report(delegation_results)

        return report

    def plan(self) -> Dict[str, Any]:
        """
        Crea un plan de auditoría detallado.
        """
        print("CAPITÁN AUDITORÍA GLOBAL: Creando plan de auditoría...")
        audit_scope = self.context.get('current_order', {}).get('details', {}).get('scope')

        planned_steps = {
            "step_1": f"definir_alcance_y_objetivos_de_la_auditoria_de_{audit_scope}",
            "step_2": "solicitar_logs_y_evidencias_a_CapitanEventosAuditoria",
            "step_3": "delegar_analisis_de_datos_y_busqueda_de_anomalias_a_tenientes_auditores",
            "step_4": "consolidar_hallazgos_y_formular_recomendaciones"
        }

        self.context['plan'] = planned_steps
        return planned_steps

    def delegate(self, plan: Dict[str, Any]) -> Dict[str, Any]:
        """
        Delega el análisis técnico a Tenientes auditores y solicita datos a otros Capitanes.
        """
        print("CAPITÁN AUDITORÍA GLOBAL: Delegando tareas de análisis de auditoría...")
        results = {}
        for step, task in plan.items():
            print(f"  - Delegando tarea: {task}")
            results[step] = {"status": "DELEGATED", "result": f"Tarea '{task}' delegada para ejecución."}

        self.context['delegation_results'] = results
        return results

    def report(self, delegation_results: Dict[str, Any]) -> Dict[str, Any]:
        """
        Reporta los hallazgos y el plan de acción resultante de la auditoría.
        """
        print("CAPITÁN AUDITORÍA GLOBAL: Preparando informe de auditoría...")

        report = {
            "captain": self.__class__.__name__,
            "order_id": self.context.get('current_order', {}).get('id', 'N/A'),
            "status": "SUCCESS",
            "result": {
                "message": "Auditoría global completada.",
                "key_finding": "Se detectó un patrón de acceso inusual en el módulo de finanzas." # Simulado
            }
        }

        print("CAPITÁN AUDITORÍA GLOBAL: Informe de auditoría listo.")
        return report
