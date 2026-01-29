# backend/apps/sadi_agent/voice_orchestrator.py
import time
import logging
import hashlib
import requests
from pathlib import Path
from django.utils import timezone
from api.models import CustomUser
from .voice_providers import SpeechToTextProvider, TextToSpeechProvider
from .semantic_engine import SemanticEngine
from .translation_service import TranslationService
from .models import VoiceInteractionLog
from apps.admin_plataforma.services.governance_kernel import GovernanceKernel

logger = logging.getLogger(__name__)

class VoiceOrchestrator:
    """
    Orquesta el flujo completo de una interacción de voz, aplicando seguridad,
    semántica y auditoría.
    """
    def __init__(self, stt_provider: SpeechToTextProvider, tts_provider: TextToSpeechProvider,
                 semantic_engine: SemanticEngine, translation_service: TranslationService,
                 api_base_url: str = "http://127.0.0.1:8000/api/sarita"):
        self.stt_provider = stt_provider
        self.tts_provider = tts_provider
        self.semantic_engine = semantic_engine
        self.translation_service = translation_service
        self.api_base_url = api_base_url

    def handle_audio_command(self, user: CustomUser, api_token: str, audio_path: Path, output_audio_path: Path) -> (str, Path):
        """
        Flujo principal de la Fase Z para manejar un comando de voz desde audio.
        """
        log = VoiceInteractionLog.objects.create(user=user)
        text_response = "Lo siento, ha ocurrido un error inesperado."
        detected_language = "es" # Default

        try:
            # 1. Transcripción y Detección de Idioma
            log.audio_hash = self._calculate_hash(audio_path)
            transcribed_text, detected_language = self.stt_provider.transcribe(audio_path)
            log.transcribed_text = transcribed_text
            log.detected_language = detected_language
            log.save()

            # 2. Normalización a Idioma Base
            normalized_text = self.translation_service.normalize_to_base_language(transcribed_text, detected_language)
            log.normalized_text = normalized_text
            log.save()

            # 3. Interpretación Semántica
            intent, entities = self.semantic_engine.interpret(normalized_text)
            if not intent:
                raise ValueError("No se pudo interpretar la intención del comando.")
            log.detected_intent = intent
            log.extracted_entities = entities
            log.save()

            # 4. Verificación de Soberanía y Autoridad (Kernel)
            log.permission_checked = True
            kernel = GovernanceKernel(user=user)

            # El Kernel valida contrato, autoridad y políticas globales
            # Si falla, lanza excepción que atrapamos abajo
            try:
                kernel._validate_authority(kernel._registry[intent.name])
                kernel._evaluate_policies(kernel._registry[intent.name], entities)
                log.permission_granted = True
            except Exception as e:
                log.permission_granted = False
                log.final_status = "REJECTED"
                log.save()
                raise PermissionError(f"Gobernanza bloqueó la acción: {str(e)}")

            log.save()

            # 5. Ejecución de la Misión (Delegación a Agentes)
            directive = self._build_directive(intent, entities)
            mission_id = self._invoke_sarita_api(directive, api_token)
            log.mission_id = mission_id
            log.save()

            final_mission_status = self._poll_mission_status(mission_id, api_token)
            text_response = self._generate_spoken_response(final_mission_status)
            log.final_status = final_mission_status.get("estado", "UNKNOWN")

        except (ValueError, PermissionError) as e:
            text_response = f"Error: {e}"
            log.final_status = "REJECTED"
        except Exception as e:
            logger.error(f"Error inesperado en el flujo de voz: {e}", exc_info=True)
            text_response = "Lo siento, ha ocurrido un error inesperado."
            log.final_status = "FAILED"

        # 6. Traducción y Síntesis de Voz de la Respuesta
        final_response_text = self.translation_service.translate_response(text_response, detected_language)
        log.text_response = final_response_text
        self.tts_provider.speak(final_response_text, output_audio_path)

        log.timestamp_end = timezone.now()
        log.save()

        return final_response_text, output_audio_path

    def _build_directive(self, intent, entities):
        return {
            "domain": intent.domain.name,
            "mission": intent.name,
            "objetivo": f"Ejecutar la intención {intent.name} con los parámetros {entities}",
            "parametros": entities,
        }

    def _calculate_hash(self, file_path: Path) -> str:
        sha256 = hashlib.sha256()
        with open(file_path, "rb") as f:
            for byte_block in iter(lambda: f.read(4096), b""):
                sha256.update(byte_block)
        return sha256.hexdigest()

    def _get_headers(self, token: str):
        return {
            "Authorization": f"Bearer {token}",
            "Content-Type": "application/json"
        }

    def _invoke_sarita_api(self, directive: dict, api_token: str) -> str:
        """
        Envía la directiva al endpoint de la API de SARITA.
        """
        url = f"{self.api_base_url}/directive/"
        headers = self._get_headers(api_token)
        logger.debug(f"Invocando API de SARITA en {url} con directiva: {directive}")

        response = requests.post(url, json=directive, headers=headers)

        if response.status_code == 202:
            mission_id = response.json().get("mission_id")
            logger.info(f"API aceptó la directiva. ID de la Misión: {mission_id}")
            return mission_id
        else:
            logger.error(f"Error al invocar la API de SARITA. Status: {response.status_code}, Body: {response.text}")
            raise ConnectionError(f"La API de SARITA devolvió un error: {response.status_code}")

    def _poll_mission_status(self, mission_id: str, api_token: str) -> dict:
        """
        Consulta el estado de la misión hasta que se complete o falle.
        """
        url = f"{self.api_base_url}/missions/{mission_id}/"
        headers = self._get_headers(api_token)
        max_retries = 30
        poll_interval = 2

        for i in range(max_retries):
            logger.debug(f"Polling para misión {mission_id}, intento {i+1}/{max_retries}")
            response = requests.get(url, headers=headers)

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
