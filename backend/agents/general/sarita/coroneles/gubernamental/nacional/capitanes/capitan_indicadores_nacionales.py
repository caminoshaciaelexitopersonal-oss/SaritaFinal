from typing import Dict, Any

class CapitanIndicadoresNacionales:
    """
    Misión: Consolidar, analizar y reportar los indicadores clave de desempeño (KPIs)
    del sector turístico a nivel nacional, como la ocupación hotelera, el gasto
    promedio de turistas y la llegada de visitantes.
    """

    def __init__(self, coronel):
        self.coronel = coronel
        self.context = {}
        print(f"CAPITÁN INDICADORES NACIONALES: Inicializado.")

    def handle_order(self, order: Dict[str, Any]) -> Dict[str, Any]:
        """
        Recibe órdenes para generar el reporte de indicadores de un período.
        """
        print(f"CAPITÁN INDICADORES NACIONALES: Orden recibida - {order['type']}")
        self.context['current_order'] = order

        plan = self.plan()
        delegation_results = self.delegate(plan)
        report = self.report(delegation_results)

        return report

    def plan(self) -> Dict[str, Any]:
        """
        Crea un plan para la recolección y consolidación de datos.
        """
        print("CAPITÁN INDICADORES NACIONALES: Creando plan de consolidación de datos...")
        period = self.context.get('current_order', {}).get('details', {}).get('period')

        planned_steps = {
            "step_1": f"solicitar_reportes_de_indicadores_a_coroneles_departamentales_para_{period}",
            "step_2": "delegar_limpieza_y_agregacion_de_datos_recibidos",
            "step_3": "calcular_kpis_nacionales_consolidados",
            "step_4": "generar_dashboard_ejecutivo"
        }

        self.context['plan'] = planned_steps
        return planned_steps

    def delegate(self, plan: Dict[str, Any]) -> Dict[str, Any]:
        """
        Delega la recolección de datos a los Coroneles Departamentales y el
        procesamiento a Tenientes analistas de datos.
        """
        print("CAPITÁN INDICADORES NACIONALES: Delegando tareas de recolección y análisis...")
        results = {}
        for step, task in plan.items():
            print(f"  - Delegando tarea: {task}")
            results[step] = {"status": "DELEGATED", "result": f"Tarea '{task}' delegada para ejecución."}

        self.context['delegation_results'] = results
        return results

    def report(self, delegation_results: Dict[str, Any]) -> Dict[str, Any]:
        """
        Reporta el informe consolidado de indicadores nacionales.
        """
        print("CAPITÁN INDICADORES NACIONALES: Preparando informe de indicadores...")

        report = {
            "captain": self.__class__.__name__,
            "order_id": self.context.get('current_order', {}).get('id', 'N/A'),
            "status": "SUCCESS",
            "result": {
                "message": "Informe de Indicadores Nacionales generado.",
                "dashboard_location": "/path/to/dashboard_nacional.pdf" # Simulado
            }
        }

        print("CAPITÁN INDICADORES NACIONALES: Informe de indicadores listo.")
        return report
