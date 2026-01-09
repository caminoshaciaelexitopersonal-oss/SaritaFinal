# backend/apps/prestadores/mi_negocio/gestion_comercial/dian_services.py
import uuid
import hashlib
from datetime import datetime

class DianService:
    """
    Simulador del servicio de la DIAN para facturación electrónica.
    """
    @staticmethod
    def enviar_factura(factura, cliente):
        """
        Simula el envío de una factura y devuelve una respuesta estructurada.
        Ahora recibe el objeto 'cliente' resuelto para un futuro uso.
        """
        # Simula una decisión aleatoria de éxito o fracaso
        # Por ahora, siempre será exitoso para los tests.
        success = True

        if success:
            timestamp = datetime.now().isoformat()
            data_to_hash = f"{factura.numero_factura}-{timestamp}".encode('utf-8')
            cufe = hashlib.sha224(data_to_hash).hexdigest()

            return {
                "success": True,
                "cufe": cufe,
                "message": "Factura aceptada por la DIAN.",
                "timestamp": timestamp,
                "xml_response": f"<xml><status>Aceptado</status><cufe>{cufe}</cufe></xml>".encode('utf-8').decode('utf-8')
            }
        else:
            return {
                "success": False,
                "cufe": None,
                "message": "Error de validación: El NIT del cliente no es válido.",
                "errors": [
                    {"code": "VAL-101", "description": "El NIT del cliente no se encuentra registrado en el RUT."}
                ]
            }
