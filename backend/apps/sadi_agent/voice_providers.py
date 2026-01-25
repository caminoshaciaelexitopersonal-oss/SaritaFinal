# backend/apps/sadi_agent/voice_providers.py
import os
import abc
from openai import OpenAI
import logging
from pathlib import Path

logger = logging.getLogger(__name__)

class SpeechToTextProvider(abc.ABC):
    """Interfaz abstracta para proveedores de Speech-to-Text."""
    @abc.abstractmethod
    def transcribe(self, audio_path: Path) -> str:
        pass

class TextToSpeechProvider(abc.ABC):
    """Interfaz abstracta para proveedores de Text-to-Speech."""
    @abc.abstractmethod
    def speak(self, text: str, output_path: Path):
        pass

# --- Implementaciones Concretas ---

class WhisperProvider(SpeechToTextProvider):
    """Implementación de STT utilizando la API de OpenAI Whisper."""
    def __init__(self, api_key: str = None):
        self.api_key = api_key or os.environ.get("OPENAI_API_KEY")
        if not self.api_key:
            raise ValueError("No se encontró la clave de API de OpenAI. Por favor, establezca la variable de entorno OPENAI_API_KEY.")
        self.client = OpenAI(api_key=self.api_key)

    def transcribe(self, audio_path: Path) -> str:
        logger.info(f"Transcribiendo archivo de audio: {audio_path}")
        if not audio_path.exists():
            raise FileNotFoundError(f"El archivo de audio no se encontró en la ruta: {audio_path}")

        try:
            with open(audio_path, "rb") as audio_file:
                transcription = self.client.audio.transcriptions.create(
                    model="whisper-1",
                    file=audio_file
                )
            logger.info(f"Transcripción exitosa. Texto: '{transcription.text}'")
            return transcription.text
        except Exception as e:
            logger.error(f"Error durante la transcripción con Whisper: {e}", exc_info=True)
            raise

class OpenAITTSProvider(TextToSpeechProvider):
    """Implementación de TTS utilizando la API de OpenAI."""
    def __init__(self, api_key: str = None, voice: str = "alloy"):
        self.api_key = api_key or os.environ.get("OPENAI_API_KEY")
        if not self.api_key:
            raise ValueError("No se encontró la clave de API de OpenAI. Por favor, establezca la variable de entorno OPENAI_API_KEY.")
        self.client = OpenAI(api_key=self.api_key)
        self.voice = voice

    def speak(self, text: str, output_path: Path):
        logger.info(f"Generando audio para el texto: '{text}' en el archivo {output_path}")
        try:
            response = self.client.audio.speech.create(
                model="tts-1",
                voice=self.voice,
                input=text
            )

            # Escribir la respuesta de audio en el archivo de salida
            response.stream_to_file(output_path)
            logger.info(f"Audio generado y guardado exitosamente en: {output_path}")
        except Exception as e:
            logger.error(f"Error durante la generación de audio con OpenAI TTS: {e}", exc_info=True)
            raise
