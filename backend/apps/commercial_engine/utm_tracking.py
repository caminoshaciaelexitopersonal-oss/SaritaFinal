import logging

logger = logging.getLogger(__name__)

class UTMTracker:
    """
    Utility to track and parse UTM parameters for Lead attribution.
    """

    @staticmethod
    def extract_utm_params(request_data: dict) -> dict:
        """
        Extrae parámetros UTM de un diccionario de datos (ej: request.GET o request.POST).
        """
        return {
            'utm_source': request_data.get('utm_source'),
            'utm_medium': request_data.get('utm_medium'),
            'utm_campaign': request_data.get('utm_campaign'),
            'utm_term': request_data.get('utm_term'),
            'utm_content': request_data.get('utm_content'),
        }

    @staticmethod
    def enrich_lead_with_utm(lead, utm_params: dict):
        """
        Enriquece un objeto Lead con parámetros UTM.
        """
        lead.utm_source = utm_params.get('utm_source', lead.utm_source)
        lead.utm_campaign = utm_params.get('utm_campaign', lead.utm_campaign)
        # Otros parámetros podrían guardarse en un JSONField si fuera necesario
        lead.save()
        return lead
