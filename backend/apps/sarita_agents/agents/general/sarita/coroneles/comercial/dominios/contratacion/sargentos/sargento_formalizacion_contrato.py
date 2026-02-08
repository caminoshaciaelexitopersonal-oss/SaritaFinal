# backend/apps/sarita_agents/agents/general/sarita/coroneles/comercial/dominios/contratacion/sargentos/sargento_formalizacion_contrato.py

from .......sargento_template import SargentoTemplate
from apps.prestadores.mi_negocio.gestion_comercial.domain.models import OperacionComercial, ContratoComercial
from django.utils import timezone
import hashlib

class SargentoFormalizacionContrato(SargentoTemplate):
    """
    Sargento de Formalización de Contrato.
    Función atómica: Crear el registro de ContratoComercial a partir de una Operación.
    """
    def perform_atomic_action(self, action_data: dict):
        operacion_id = action_data.get("operacion_id")
        try:
            operacion = OperacionComercial.objects.get(id=operacion_id)
        except OperacionComercial.DoesNotExist:
            raise ValueError(f"Operación {operacion_id} no encontrada.")

        # Generar hash de firma (Simulado para Fase 1)
        payload_firma = f"{operacion.id}-{operacion.total}-{timezone.now()}"
        hash_firma = hashlib.sha256(payload_firma.encode()).hexdigest()

        contrato = ContratoComercial.objects.create(
            operacion=operacion,
            perfil_ref_id=operacion.perfil_ref_id,
            cliente_ref_id=operacion.cliente_ref_id,
            terminos_y_condiciones=action_data.get("terminos", "Términos estándar de SARITA."),
            fecha_firma=timezone.now(),
            hash_firma_digital=hash_firma,
            estado=ContratoComercial.EstadoContrato.FIRMADO
        )

        return {
            "contrato_id": str(contrato.id),
            "hash_firma": hash_firma,
            "estado": contrato.estado
        }
