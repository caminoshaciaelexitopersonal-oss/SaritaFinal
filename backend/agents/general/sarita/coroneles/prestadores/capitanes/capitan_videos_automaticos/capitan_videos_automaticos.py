from typing import Dict, Any

class CapitanVideosAutomaticos:
    """
    Misión: Orquestar el proceso completo de creación y publicación de videos
    comerciales generados por IA, desde el guion hasta el análisis de resultados.
    """

    def __init__(self, coronel):
        self.coronel = coronel
        self.context = {}
        print(f"CAPITÁN VIDEOS AUTOMÁTICOS: Inicializado.")

    def handle_order(self, order: Dict[str, Any]) -> Dict[str, Any]:
        """
        Recibe órdenes para generar un video sobre un tema o producto.
        """
        print(f"CAPITÁN VIDEOS AUTOMÁTICOS: Orden recibida - {order['type']}")
        self.context['current_order'] = order

        plan = self.plan()
        delegation_results = self.delegate(plan)
        report = self.report(delegation_results)

        return report

    def plan(self) -> Dict[str, Any]:
        """
        Crea un plan de producción de video de principio a fin.
        """
        print("CAPITÁN VIDEOS AUTOMÁTICOS: Creando plan de producción de video...")

        planned_steps = {
            "step_1": {"teniente": "guiones_video", "task": "generar_guion_desde_producto"},
            "step_2": {"teniente": "generacion_video", "task": "renderizar_video_borrador"},
            "step_3": {"teniente": "edicion_automatica", "task": "anadir_branding_y_logo"},
            "step_4": {"teniente": "publicacion_video", "task": "publicar_con_copy_y_hashtags"},
            "step_5": {"teniente": "analitica_video", "task": "reportar_engagement_y_ctr"}
        }

        self.context['plan'] = planned_steps
        return planned_steps

    def delegate(self, plan: Dict[str, Any]) -> Dict[str, Any]:
        """
        Delega cada fase de la producción a su teniente especialista.
        """
        print("CAPITÁN VIDEOS AUTOMÁTICOS: Delegando producción de video...")
        results = {}
        for step, details in plan.items():
            print(f"  - Delegando tarea '{details['task']}' a Teniente '{details['teniente']}'")
            results[step] = {"status": "DELEGATED", "result": "Tarea simulada completada por teniente."}

        self.context['delegation_results'] = results
        return results

    def report(self, delegation_results: Dict[str, Any]) -> Dict[str, Any]:
        """
        Reporta la finalización del ciclo de producción de video.
        """
        print("CAPITÁN VIDEOS AUTOMÁTICOS: Preparando informe de producción...")

        report = {
            "captain": self.__class__.__name__,
            "order_id": self.context.get('current_order', {}).get('id', 'N/A'),
            "status": "SUCCESS",
            "summary": "Producción y publicación de video completada."
        }

        print("CAPITÁN VIDEOS AUTOMÁTICOS: Informe listo.")
        return report
