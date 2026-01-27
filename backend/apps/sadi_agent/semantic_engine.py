# backend/apps/sadi_agent/semantic_engine.py
import logging
import re
from typing import Tuple, Dict, Optional
from .models import Intent, Example

logger = logging.getLogger(__name__)

class SemanticEngine:
    """
    Motor para interpretar la intención y extraer entidades del texto.
    """

    def interpret(self, text: str) -> Tuple[Optional[Intent], Dict]:
        """
        Interpreta el texto para encontrar la intención y extraer entidades.

        Returns:
            Una tupla de (Intent, dict_de_entidades) o (None, {}) si no se encuentra.
        """
        logger.debug(f"Interpretando texto: '{text}'")

        # 1. Encontrar la intención basada en los ejemplos
        # Usamos una coincidencia simple por ahora. En una versión avanzada,
        # se podría usar búsqueda de texto completo, embeddings o un modelo de NLU.

        # Normalizamos el texto de entrada para una coincidencia más robusta
        normalized_text = self._normalize_text(text)

        matched_intent = None
        # Iteramos sobre los ejemplos para encontrar una coincidencia
        for example in Example.objects.all():
            normalized_example = self._normalize_text(example.text)
            # Simplificamos: si el texto del ejemplo está en el comando del usuario
            # (ignorando mayúsculas/minúsculas y puntuación), asumimos una coincidencia.
            # Esto es un placeholder; la lógica real sería más compleja.

            # Para esta fase, usaremos un método de coincidencia de palabras clave.
            if self._keywords_match(normalized_example, normalized_text):
                matched_intent = example.intent
                break

        if not matched_intent:
            logger.warning(f"No se pudo encontrar una intención para el texto: '{text}'")
            return None, {}

        logger.info(f"Intención encontrada: '{matched_intent.name}'")

        # 2. Extraer entidades basadas en la intención
        entities = self._extract_entities(text, matched_intent)

        return matched_intent, entities

    def _normalize_text(self, text: str) -> str:
        """
        Convierte el texto a minúsculas y elimina caracteres no alfanuméricos
        para facilitar la comparación.
        """
        return re.sub(r'[^\w\s]', '', text.lower())

    def _keywords_match(self, example_text: str, user_text: str) -> bool:
        """
        Comprueba si las palabras clave del ejemplo están en el texto del usuario.
        """
        # Un enfoque simple: si las palabras clave "registra", "hotel", "correo" están presentes.
        # Esto debe ser específico para la intención.
        keywords = ["registra", "hotel", "correo", "dar", "alta", "proveedor", "email"]
        return all(keyword in user_text for keyword in self._get_keywords(example_text, keywords))

    def _get_keywords(self, text:str, keywords: list) -> list:
        """
        Extrae las palabras clave relevantes de un texto.
        """
        return [word for word in text.split() if word in keywords]


    def _extract_entities(self, text: str, intent: Intent) -> Dict:
        """
        Extrae entidades del texto usando regex, basado en la intención.
        """
        entities = {}
        if intent.name == 'ONBOARDING_PRESTADOR':
            # Regex para el nombre (lo que está entre comillas)
            name_match = re.search(r"'(.*?)'", text, re.IGNORECASE)
            if name_match:
                entities['nombre_comercial'] = name_match.group(1).title()

            # Regex para el correo electrónico
            email_match = re.search(r'[\w\.\-]+@[\w\.\-]+', text, re.IGNORECASE)
            if email_match:
                entities['email'] = email_match.group(0)

        logger.info(f"Entidades extraídas: {entities}")
        return entities
