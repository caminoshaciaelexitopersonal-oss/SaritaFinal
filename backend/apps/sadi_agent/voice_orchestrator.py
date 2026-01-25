# backend/apps/sadi_agent/voice_orchestrator.py
import re
import time
import requests
import logging

logger = logging.getLogger(__name__)

class VoiceOrchestrator:
    """
    Punto de entrada para los comandos de voz.
    Transcribe, interpreta, invoca la API de SARITA y genera una respuesta hablada.
    """
    def __init__(self, api_token: str, api_base_url: str = "http://127.0.0.1:8000/api/sarita"):
        self.api_token = api_token
        self.api_base_url = api_base_url
        self.headers = {
            "Authorization": f"Token {self.api_token}",
            "Content-Type": "application/json",
        }

    def handle_voice_command(self, text: str) -> str:
        """
        Flujo principal para manejar un comando de voz de extremo a extremo.
        """
        logger.info(f"VOICE ORCHESTRATOR: Comando recibido -> '{text}'")

        try:
            # 1. Interpretar intención y generar directiva
            directive = self._translate_intent_to_directive(text)
            logger.info(f"Directiva generada: {directive}")

            # 2. Invocar la API de SARITA para iniciar la misión
            mission_id = self._invoke_sarita_api(directive)
            logger.info(f"Misión {mission_id} iniciada a través de la API.")

            # 3. Monitorear el estado de la misión (polling)
            final_mission_status = self._poll_mission_status(mission_id)
            logger.info(f"Misión {mission_id} finalizada con estado: {final_mission_status['estado']}")

            # 4. Generar respuesta hablada
            spoken_response = self._generate_spoken_response(final_mission_status)
            logger.info(f"Respuesta generada: {spoken_response}")

            return spoken_response

        except ValueError as e:
            logger.error(f"Error de validación o interpretación: {e}")
            return f"Error: {e}"
        except Exception as e:
            logger.error(f"Error inesperado en el flujo de voz: {e}", exc_info=True)
            return "Lo siento, ha ocurrido un error inesperado."

    def _translate_intent_to_directive(self, text: str) -> dict:
        """
        Simula un LLM para traducir texto a una directiva SARITA estructurada.
        Utiliza reglas simples para la misión de onboarding de prestadores.
        """
        logger.debug(f"Traduciendo intent del texto: '{text}'")

        # Patrón para registrar un nuevo prestador
        pattern = r"registrar un nuevo prestador.*se llama '(.*)'.*NIT es ([\d\.\-]+)"
        match = re.search(pattern, text, re.IGNORECASE)

        if match:
            nombre = match.group(1)
            nit = match.group(2)
            logger.info(f"Intención 'onboard_prestador' reconocida. Nombre: {nombre}, NIT: {nit}")

            directive = {
                "mision": "onboard_prestador",
                "objetivo": f"Registrar al prestador '{nombre}' con NIT {nit} en el sistema.",
                "parametros": {
                    "nombre_comercial": nombre,
                    "nit": nit
                }
            }
            return directive

        logger.warning(f"No se pudo reconocer una intención válida en el comando: '{text}'")
        raise ValueError("No se pudo interpretar el comando de voz. Por favor, intente de nuevo.")

    def _invoke_sarita_api(self, directive: dict) -> str:
        """
        Envía la directiva al endpoint de la API de SARITA.
        """
        url = f"{self.api_base_url}/directive/"
        logger.debug(f"Invocando API de SARITA en {url} con directiva: {directive}")

        response = requests.post(url, json=directive, headers=self.headers)

        if response.status_code == 202:
            mission_id = response.json().get("mission_id")
            logger.info(f"API aceptó la directiva. ID de la Misión: {mission_id}")
            return mission_id
        else:
            logger.error(f"Error al invocar la API de SARITA. Status: {response.status_code}, Body: {response.text}")
            raise ConnectionError(f"La API de SARITA devolvió un error: {response.status_code}")

    def _poll_mission_status(self, mission_id: str) -> dict:
        """
        Consulta el estado de la misión hasta que se complete o falle.
        """
        url = f"{self.api_base_url}/missions/{mission_id}/"
        max_retries = 30
        poll_interval = 2

        for i in range(max_retries):
            logger.debug(f"Polling para misión {mission_id}, intento {i+1}/{max_retries}")
            response = requests.get(url, headers=self.headers)

            if response.status_code == 200:
                status_data = response.json()
                estado = status_data.get("estado")

                if estado in ["EJECUTANDO", "PENDIENTE"]:
                    time.sleep(poll_interval)
                    continue
                else:
                    logger.info(f"Misión {mission_id} alcanzó el estado final: {estado}")
                    return status_data
            else:
                logger.error(f"Error al consultar estado de la misión {mission_id}. Status: {response.status_code}")
                raise ConnectionError(f"Error al consultar el estado de la misión: {response.status_code}")

        raise TimeoutError(f"La misión {mission_id} no finalizó en el tiempo esperado.")

    def _generate_spoken_response(self, mission_status: dict) -> str:
        """
        Genera una respuesta en lenguaje natural basada en el estado final de la misión.
        """
        estado = mission_status.get("estado")
        reporte_final = mission_status.get("reporte_final", "No hay un reporte detallado.")

        if estado == "COMPLETADA":
            return f"Misión completada con éxito. {reporte_final}"
        elif estado == "FALLIDA":
            return f"La misión ha fallado. Razón: {reporte_final}"
        elif estado == "CANCELADA":
            return "La misión fue cancelada."
        else:
            return f"La misión terminó en un estado inesperado: {estado}. Por favor, revise los registros."
