# backend/apps/prestadores/mi_negocio/gestion_comercial/dian_services.py
import random
import uuid
from decimal import Decimal

class DianService:
    """
    Servicio Stub para simular la interacción con la DIAN.
    En una implementación real, este servicio contendría la lógica para:
    1. Construir el XML de la factura electrónica.
    2. Firmar digitalmente el XML.
    3. Enviar el XML a un proveedor tecnológico o directamente a la DIAN.
    4. Procesar la respuesta para obtener el CUFE y el track_id.
    """

    @staticmethod
    def enviar_factura(factura):
        """
        Simula el envío de una factura a la DIAN.

        Args:
            factura: La instancia de FacturaVenta a enviar.

        Returns:
            Un diccionario con el resultado de la simulación.
            Ejemplo de éxito:
            {
                "success": True,
                "cufe": "c1a2b3...",
                "track_id": "xyz-789...",
                "xml": "<xml>...</xml>",
                "pdf": b"...",
                "message": "Factura enviada y aceptada por la DIAN."
            }
            Ejemplo de error:
            {
                "success": False,
                "errors": ["Error de validación: El NIT del receptor no es válido."],
                "message": "La factura fue rechazada por la DIAN."
            }
        """
        # Simular una tasa de fallo del 20%
        if random.random() < 0.2:
            return {
                "success": False,
                "errors": [
                    "Error 99: Firma digital inválida.",
                    "Error 12: El consecutivo de la factura ya fue utilizado."
                ],
                "message": "La factura fue rechazada por la DIAN por errores de validación."
            }

        # Simular una respuesta exitosa
        return {
            "success": True,
            "cufe": str(uuid.uuid4()),
            "track_id": f"track-{random.randint(1000, 9999)}",
            "xml": f"<Invoice><ID>{factura.numero_factura}</ID><Total>{factura.total}</Total></Invoice>",
            "pdf": b"%PDF-1.4...", # Contenido simulado de un PDF
            "message": "Factura enviada y aceptada exitosamente por la DIAN."
        }
