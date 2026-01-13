from typing import Dict, Any

class CapitanEnlacesLlm:
    """
    Misión: Actuar como una capa de abstracción para conectar el sistema Sarita
    con agentes LLM externos o internos, orquestando la generación de contenido
    multimodal (texto, audio, video).
    """

    def __init__(self, coronel):
        self.coronel = coronel
        self.context = {}
        print(f"CAPITÁN ENLACES LLM: Inicializado.")

    def handle_order(self, order: Dict[str, Any]) -> Dict[str, Any]:
        """
        Recibe órdenes de alto nivel para la creación de contenido.
        """
        print(f"CAPITÁN ENLACES LLM: Orden recibida - {order['type']}")
        self.context['current_order'] = order

        plan = self.plan()
        delegation_results = self.delegate(plan)
        report = self.report(delegation_results)

        return report

    def plan(self) -> Dict[str, Any]:
        """
        Crea un plan de generación de contenido utilizando LLMs.
        """
        print("CAPITÁN ENLACES LLM: Creando plan de generación de contenido...")
        order_type = self.context.get('current_order', {}).get('type')

        planned_steps = {}
        if order_type == "generar_video_promocional_completo":
            planned_steps = {
                "step_1": {"teniente": "orquestacion_llm", "task": "orquestar_texto_a_video_completo"}
            }

        self.context['plan'] = planned_steps
        return planned_steps

    def delegate(self, plan: Dict[str, Any]) -> Dict[str, Any]:
        """
        Delega la ejecución de la cadena de generación a sus tenientes LLM.
        """
        print("CAPITÁN ENLACES LLM: Delegando a tenientes LLM...")
        results = {}
        for step, details in plan.items():
            print(f"  - Delegando tarea '{details['task']}' a Teniente '{details['teniente']}'")
            results[step] = {"status": "DELEGATED", "result": "Generación LLM simulada completada."}

        self.context['delegation_results'] = results
        return results

    def report(self, delegation_results: Dict[str, Any]) -> Dict[str, Any]:
        """
        Reporta la finalización de la generación de contenido.
        """
        print("CAPITÁN ENLACES LLM: Preparando informe de contenido generado...")

        report = {
            "captain": self.__class__.__name__,
            "order_id": self.context.get('current_order', {}).get('id', 'N/A'),
            "status": "SUCCESS",
            "summary": "Contenido generado por IA listo para usar."
        }

        print("CAPITÁN ENLACES LLM: Informe listo.")
        return report
