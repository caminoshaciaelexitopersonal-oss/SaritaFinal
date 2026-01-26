# backend/apps/sadi_agent/translation_service.py
import logging
from googletrans import Translator, LANGUAGES

logger = logging.getLogger(__name__)

class TranslationService:
    """
    Servicio para manejar la traducción de texto.
    """
    def __init__(self, base_language='es'):
        self.translator = Translator()
        self.base_language = base_language

    def normalize_to_base_language(self, text: str, source_language: str) -> str:
        """
        Traduce el texto al idioma base del sistema (español).
        """
        if source_language == self.base_language:
            return text

        logger.debug(f"Normalizando texto de '{source_language}' a '{self.base_language}': '{text}'")
        try:
            translated = self.translator.translate(text, dest=self.base_language, src=source_language)
            logger.info(f"Texto normalizado: '{translated.text}'")
            return translated.text
        except Exception as e:
            logger.error(f"Error durante la normalización: {e}", exc_info=True)
            # Fallback: devolver el texto original si la traducción falla
            return text

    def translate_response(self, text: str, target_language: str) -> str:
        """
        Traduce la respuesta del sistema al idioma de destino del usuario.
        """
        if target_language == self.base_language:
            return text

        logger.debug(f"Traduciendo respuesta a '{target_language}': '{text}'")
        try:
            # Asegurarse de que el idioma de destino es válido
            if target_language not in LANGUAGES:
                logger.warning(f"Idioma de destino '{target_language}' no válido. Usando idioma base.")
                return text

            translated = self.translator.translate(text, dest=target_language, src=self.base_language)
            logger.info(f"Respuesta traducida: '{translated.text}'")
            return translated.text
        except Exception as e:
            logger.error(f"Error durante la traducción de la respuesta: {e}", exc_info=True)
            # Fallback: devolver el texto original si la traducción falla
            return text
