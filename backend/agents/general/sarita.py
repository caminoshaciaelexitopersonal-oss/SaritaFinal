"""
Módulo Principal del Agente General Sarita.

Este archivo contiene la clase `SaritaGeneral`, que actúa como el punto de entrada
y el cerebro cognitivo central para todo el sistema de agentes de IA.
"""

class SaritaGeneral:
    """
    El Comandante Cognitivo del sistema Sarita.

    Esta clase no ejecuta tareas de negocio directamente. Su única responsabilidad
    es recibir órdenes, interpretarlas, decidir qué dominio es el responsable
    y delegar la ejecución a un agente Coronel especializado.
    """

    def __init__(self):
        """
        Inicializa el Agente General.
        Aquí se cargarían los componentes como el parser, router, memoria, etc.
        """
        print("General Sarita: Online y lista para recibir órdenes.")
        # self.intent_parser = IntentParser()
        # self.router = Router()
        # self.memory = Memory()
        # self.context = Context()

    def receive_order(self, raw_input: str, user_context: dict):
        """
        Punto único de entrada de órdenes al sistema de agentes.

        Args:
            raw_input (str): La orden en lenguaje natural del usuario.
            user_context (dict): Metadatos sobre el usuario (ID, rol, vía, etc.).

        Returns:
            dict: Un reporte del resultado de la operación.
        """
        print(f"Orden recibida: '{raw_input}' con contexto: {user_context}")

        # 1. Analizar Intención
        intent = self.analyze_intent(raw_input, user_context)

        # 2. Determinar Dominio (Enrutamiento)
        command = self.determine_domain(intent, user_context)

        # 3. Delegar al Coronel
        report = self.delegate_to_coronel(command)

        # 4. Recibir y procesar reporte
        final_response = self.receive_report(report)

        return final_response

    def analyze_intent(self, raw_input: str, context: dict) -> dict:
        """
        Utiliza componentes de NLP (simulados por ahora) para comprender la intención.

        En una implementación real, aquí se llamaría a OpenManus o similar.
        """
        print("Analizando intención...")
        # Simulación: se extrae una intención estructurada
        intent = {
            "action": "crear",
            "entity": "factura",
            "details": "cliente VIP, producto X, 10 unidades",
            "raw": raw_input
        }
        print(f"Intención identificada: {intent}")
        return intent

    def determine_domain(self, intent: dict, context: dict) -> dict:
        """
        Decide qué Coronel debe recibir la orden basado en la intención y el contexto.
        """
        print("Determinando dominio y Coronel responsable...")
        # Simulación de lógica de enrutamiento
        domain = "comercial" # Lógica de router iría aquí

        command = {
            "domain": domain,
            "intent": intent,
            "user_context": context,
            "target_coronel": f"coronel_{domain}"
        }
        print(f"Dominio decidido: {domain}. Comando preparado para el Coronel.")
        return command

    def delegate_to_coronel(self, command: dict) -> dict:
        """
        Envía el comando estructurado al Coronel correspondiente.
        """
        target = command.get("target_coronel")
        print(f"Delegando comando al {target}...")

        # Simulación: Aquí se llamaría al método del Coronel
        # Ejemplo: coronel_comercial.execute_command(command)

        # Simulación de respuesta del Coronel
        report = {
            "status": "SUCCESS",
            "message": f"Orden ejecutada por {target}: Factura creada exitosamente.",
            "data": {"factura_id": "F-2024-001"}
        }

        print("Delegación completada. Esperando reporte...")
        return report

    def receive_report(self, report: dict) -> dict:
        """
        Recibe el resultado final del Coronel y lo formatea para el usuario.
        """
        print(f"Reporte recibido del Coronel: {report}")
        # Lógica para manejar el reporte, loguear, y preparar respuesta final

        return {
            "user_message": report.get("message"),
            "status_code": 200 if report.get("status") == "SUCCESS" else 500
        }

# Ejemplo de uso (para pruebas directas)
if __name__ == '__main__':
    general_sarita = SaritaGeneral()

    test_order = "Necesito crear una nueva factura para el cliente VIP"
    test_context = {"user_id": 123, "rol": "empresario", "via": "prestador"}

    final_result = general_sarita.receive_order(test_order, test_context)

    print("\n--- Resultado Final ---")
    print(final_result)
    print("-----------------------")
