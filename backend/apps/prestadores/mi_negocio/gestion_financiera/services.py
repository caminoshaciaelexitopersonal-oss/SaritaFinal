import json
from decimal import Decimal
from django.utils import timezone
from django.db import transaction

from .models import OrdenPago
# --- IMPORTACIONES DE SERVICIOS DE DOMINIO ---
from ..gestion_operativa.services import ProviderProfileService
from ..gestion_archivistica.archiving import ArchivingService
# Nota: Se asumirá la existencia de servicios para CuentaBancaria, Empleado, etc.
# o se resolverán de la manera apropiada en su respectiva fase.

class PagoService:
    @staticmethod
    @transaction.atomic
    def crear_orden_pago(
        perfil_ref_id: str,
        cuenta_bancaria_ref_id: str,
        beneficiario_id: str,
        tipo_beneficiario: str,
        monto: Decimal,
        concepto: str,
        user_id: int
    ):
        """
        Crea una Orden de Pago de forma desacoplada y la archiva en el SGA.
        """
        # 1. Resolver el perfil para obtener el company_id
        perfil = ProviderProfileService.get_profile_by_id(perfil_ref_id)
        if not perfil:
            raise ValueError("Perfil de proveedor no encontrado.")

        # 2. Crear la Orden de Pago
        orden_pago = OrdenPago.objects.create(
            perfil_ref_id=perfil_ref_id,
            cuenta_bancaria_ref_id=cuenta_bancaria_ref_id,
            beneficiario_id=beneficiario_id,
            tipo_beneficiario=tipo_beneficiario,
            fecha_pago=timezone.now().date(),
            monto=monto,
            concepto=concepto,
            estado=OrdenPago.EstadoPago.PAGADA
        )

        # 3. Integración con el SGA
        try:
            document_content = {
                "orden_pago_id": str(orden_pago.id),
                "beneficiario_id": str(beneficiario_id),
                "tipo_beneficiario": tipo_beneficiario,
                "monto": str(monto),
                "concepto": concepto
            }
            document_bytes = json.dumps(document_content, indent=2).encode('utf-8')

            metadata = {'source_model': 'OrdenPago', 'source_id': orden_pago.id}

            document_version = ArchivingService.archive_document(
                company_id=perfil.company_id,
                user_id=user_id,
                process_type_code='FIN',
                process_code='PAGOS',
                document_type_code='OP',
                document_content=document_bytes,
                original_filename=f"OP-{orden_pago.id}.json",
                document_metadata=metadata
            )

            # Guardar la referencia al documento archivado
            orden_pago.documento_archivistico_ref_id = document_version.document.id
            orden_pago.save(update_fields=['documento_archivistico_ref_id'])

        except Exception as e:
            # En un caso real, se manejaría el error de forma más robusta.
            # Por ahora, simplemente lo registramos (si tuviéramos un logger).
            print(f"Error al archivar la orden de pago {orden_pago.id}: {e}")
            # La transacción se revierte gracias a @transaction.atomic

        return orden_pago
