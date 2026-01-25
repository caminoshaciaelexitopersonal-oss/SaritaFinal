# backend/apps/sadi_agent/voice_orchestrator.py
import re
import time
import requests
import logging
from pathlib import Path
from .voice_providers import SpeechToTextProvider, TextToSpeechProvider

logger = logging.getLogger(__name__)

class VoiceOrchestrator:
    """
    Punto de entrada para los comandos de voz.
    Orquesta la transcripción, interpretación, ejecución de la misión y respuesta hablada.
    """
    def __init__(self, api_token: str, stt_provider: SpeechToTextProvider, tts_provider: TextToSpeechProvider, api_base_url: str = "http://127.0.0.1:8000/api/sarita"):
        self.api_token = api_token
        self.stt_provider = stt_provider
        self.tts_provider = tts_provider
        self.api_base_url = api_base_url
        self.headers = {
            "Authorization": f"Token {self.api_token}",
            "Content-Type": "application/json",
        }

    def handle_audio_command(self, audio_path: Path, output_audio_path: Path) -> (str, Path):
        """
        Flujo principal para manejar un comando de voz desde un archivo de audio.
        """
        logger.info(f"VOICE ORCHESTRATOR: Procesando comando de audio desde -> '{audio_path}'")

        # 1. Transcribir audio a texto
        transcribed_text = self.stt_provider.transcribe(audio_path)

        # 2. Procesar el texto para obtener una respuesta
        text_response = self.handle_text_command(transcribed_text)

        # 3. Convertir la respuesta de texto a audio
        self.tts_provider.speak(text_response, output_audio_path)

        return text_response, output_audio_path

    def handle_text_command(self, text: str) -> str:
        """
        Flujo principal para manejar un comando basado en texto (simulado o post-transcripción).
        """
        logger.info(f"VOICE ORCHESTRATOR: Procesando comando de texto -> '{text}'")

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
        Maneja múltiples patrones y casos de ambigüedad.
        """
        logger.debug(f"Traduciendo intent del texto: '{text}'")
        text_lower = text.lower()

        # Caso 1: Registrar hotel con nombre y correo (nuevo)
        pattern_hotel = r"registra un hotel llamado '(.*?)' con correo ([\w\.\-]+@[\w\.\-]+)"
        match_hotel = re.search(pattern_hotel, text_lower)
        if match_hotel:
            nombre = match_hotel.group(1)
            correo = match_hotel.group(2)
            logger.info(f"Intención 'onboard_prestador' (Hotel) reconocida. Nombre: {nombre}, Correo: {correo}")
            return {
                "domain": "prestadores",
                "mission": "onboard_prestador",
                "objetivo": f"Registrar al prestador tipo hotel '{nombre}' con correo {correo}.",
                "parametros": {
                    "nombre_comercial": nombre.title(),
                    "email": correo,
                    "tipo_prestador": "hotel"
                }
            }

        # Caso 2: Registrar prestador con nombre y NIT (compatibilidad)
        pattern_prestador = r"llama '(.*?)'.*NIT es ([\d\.\-]+)"
        match_prestador = re.search(pattern_prestador, text_lower, re.IGNORECASE)
        if match_prestador:
            nombre = match_prestador.group(1)
            nit = match_prestador.group(2)
            logger.info(f"Intención 'onboard_prestador' (Genérico) reconocida. Nombre: {nombre}, NIT: {nit}")
            return {
                "mision": "onboard_prestador",
                "objetivo": f"Registrar al prestador '{nombre}' con NIT {nit}.",
                "parametros": {
                    "nombre_comercial": nombre.title(),
                    "nit": nit
                }
            }

        # Caso 3: Ambigüedad
        if text_lower.strip() in ["registra un hotel", "registrar un hotel"]:
            logger.warning(f"Comando ambiguo detectado: '{text}'")
            raise ValueError("Comando incompleto. Por favor, especifique el nombre y el correo electrónico del hotel.")

        # Si ningún patrón coincide
        logger.warning(f"No se pudo reconocer una intención válida en el comando: '{text}'")
        raise ValueError("No se pudo interpretar el comando de voz. Por favor, sea más específico.")

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
