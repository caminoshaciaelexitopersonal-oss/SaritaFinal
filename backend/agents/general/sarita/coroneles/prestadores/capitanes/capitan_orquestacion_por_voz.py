from typing import Dict, Any

class CapitanOrquestacionPorVoz:
    """
    Misión: Traducir comandos de voz en órdenes estructuradas que los demás
    capitanes puedan entender y ejecutar, actuando como interfaz principal
    para la interacción por voz.
    """

    def __init__(self, coronel):
        self.coronel = coronel
        self.context = {}
        print(f"CAPITÁN ORQUESTACIÓN POR VOZ: Inicializado.")

    def handle_order(self, order: Dict[str, Any]) -> Dict[str, Any]:
        """
        Recibe un comando de voz transcrito y lo procesa.
        """
        print(f"CAPITÁN ORQUESTACIÓN POR VOZ: Orden recibida - {order['type']}")
        self.context['current_order'] = order

        plan = self.plan()
        delegation_results = self.delegate(plan)
        report = self.report(delegation_results)

        return report

    def plan(self) -> Dict[str, Any]:
        """
        Crea un plan para interpretar la intención del comando de voz.
        """
        print("CAPITÁN ORQUESTACIÓN POR VOZ: Creando plan de interpretación de voz...")
        voice_command = self.context.get('current_order', {}).get('details', {}).get('command_text')

        planned_steps = {
            "step_1": f"analizar_intencion_y_entidades_en_'{voice_command}'",
            "step_2": "mapear_intencion_a_capitan_y_orden_especifica",
            "step_3": "estructurar_orden_formal_para_el_capitan_destino",
            "step_4": "validar_parametros_requeridos_antes_de_delegar"
        }

        self.context['plan'] = planned_steps
        return planned_steps

    def delegate(self, plan: Dict[str, Any]) -> Dict[str, Any]:
        """
        Delega la orden estructurada al Capitán General del dominio correspondiente.
        """
        print("CAPITÁN ORQUESTACIÓN POR VOZ: Delegando orden interpretada...")
        results = {}
        # Simula la delegación a un Capitán General, por ejemplo, el Comercial.
        # En una implementación real, aquí se llamaría al método `handle_order`
        # del capitán correspondiente (e.g., self.coronel.capitan_gestion_comercial_general.handle_order(...))
        task = "enviar_orden_estructurada_a_CapitanGestionComercialGeneral"
        results["step_1"] = {"status": "DELEGATED_TO_CAPTAIN", "result": f"Tarea '{task}' delegada exitosamente."}

        self.context['delegation_results'] = results
        return results

    def report(self, delegation_results: Dict[str, Any]) -> Dict[str, Any]:
        """
        Reporta la confirmación de que el comando de voz fue entendido y delegado.
        """
        print("CAPITÁN ORQUESTACIÓN POR VOZ: Preparando confirmación de comando...")

        report = {
            "captain": self.__class__.__name__,
            "order_id": self.context.get('current_order', {}).get('id', 'N/A'),
            "status": "SUCCESS",
            "result": {
                "message": "Comando de voz procesado y en ejecución.",
                "interpreted_action": "Solicitud de aumento de ventas enviada al dominio comercial." # Simulado
            }
        }

        print("CAPITÁN ORQUESTACIÓN POR VOZ: Confirmación lista.")
        return report
