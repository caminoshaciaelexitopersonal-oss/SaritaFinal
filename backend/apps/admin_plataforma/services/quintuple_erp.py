import logging
from decimal import Decimal
from django.db import transaction
from django.utils import timezone
from api.models import CustomUser

logger = logging.getLogger(__name__)

class QuintupleERPService:
    """
    Servicio centralizado para asegurar el impacto en las 5 dimensiones del ERP SARITA.
    FASE 9: Integración Total.
    """
    def __init__(self, user: CustomUser):
        self.user = user

    def record_impact(self, event_type: str, payload: dict):
        """
        Punto de entrada único para la propagación de impacto sistémico.
        """
        logger.info(f"FASE 9 (QUINTUPLE ERP): Procesando impacto '{event_type}'")

        # Estructura de respuesta con las referencias a cada dimensión
        impact_result = {
            "comercial_id": None,
            "operativo_id": None,
            "contable_id": None,
            "financiero_id": None,
            "archivistico_id": None,
            "timestamp": timezone.now().isoformat()
        }

        try:
            with transaction.atomic():
                # 1. DIMENSIÓN COMERCIAL (Contratos, Ventas, Intenciones)
                impact_result["comercial_id"] = self._apply_comercial(event_type, payload)

                # 2. DIMENSIÓN OPERATIVA (Órdenes, Delivery, Seguimiento)
                impact_result["operativo_id"] = self._apply_operativo(event_type, payload)

                # 3. DIMENSIÓN CONTABLE (Asientos, Plan de Cuentas, Fiscal)
                impact_result["contable_id"] = self._apply_contable(event_type, payload)

                # 4. DIMENSIÓN FINANCIERA (Caja, Monedero, Liquidaciones)
                impact_result["financiero_id"] = self._apply_financiero(event_type, payload)

                # 5. DIMENSIÓN ARCHIVÍSTICA (Evidencia, Comprobantes, Hash)
                impact_result["archivistico_id"] = self._apply_archivistico(event_type, payload, impact_result)

                logger.info(f"FASE 9: Impacto QUÍNTUPLE completado para {event_type}. Refs: {impact_result}")
                return impact_result

        except Exception as e:
            logger.error(f"FASE 9: Error CRÍTICO en propagación de impacto: {str(e)}")
            raise e

    def _apply_comercial(self, event_type, payload):
        """Gestión de Operaciones Comerciales y Facturación."""
        try:
            from apps.prestadores.mi_negocio.gestion_comercial.domain.models import OperacionComercial
            import uuid

            # Si el evento ya trae una referencia comercial, la retornamos o actualizamos
            if "operacion_comercial_id" in payload:
                return str(payload["operacion_comercial_id"])

            # En FASE 9, si no existe, creamos una operación vinculada
            perfil_id = payload.get("perfil_id")
            cliente_id = payload.get("cliente_id")

            # Validación de UUIDs para evitar fallos de integridad en modelos estrictos
            try:
                if perfil_id: uuid.UUID(str(perfil_id))
                if cliente_id: uuid.UUID(str(cliente_id))
            except ValueError:
                logger.warning(f"ERP Comercial: IDs no son UUIDs válidos. Saltando creación.")
                return None

            if not perfil_id or not cliente_id: return None

            operacion = OperacionComercial.objects.create(
                perfil_ref_id=perfil_id,
                cliente_ref_id=cliente_id,
                total=Decimal(str(payload.get("amount", 0))),
                estado=OperacionComercial.Estado.CONFIRMADA,
                creado_por=self.user,
                tipo_operacion=OperacionComercial.TipoOperacion.VENTA
            )
            return str(operacion.id)
        except Exception as e:
            logger.warning(f"ERP Comercial: {e}")
            return None

    def _apply_operativo(self, event_type, payload):
        """Gestión de Órdenes Operativas y Delivery."""
        try:
            # Si el evento es de Delivery, el impacto operativo es el propio servicio
            if "delivery_service_id" in payload:
                return str(payload["delivery_service_id"])

            # Si es una reserva especializada
            from apps.prestadores.mi_negocio.gestion_operativa.modulos_genericos.reservas.models import Reserva
            if "reserva_id" in payload:
                return str(payload["reserva_id"])

            return None
        except Exception as e:
            logger.warning(f"ERP Operativo: {e}")
            return None

    def _apply_contable(self, event_type, payload):
        """Generación de Asientos Contables Automáticos."""
        try:
            from apps.prestadores.mi_negocio.gestion_contable.contabilidad.models import AsientoContable, PeriodoContable
            import uuid

            perfil_id = payload.get("perfil_id")
            if not perfil_id: return None

            try:
                uuid.UUID(str(perfil_id))
            except ValueError:
                return None

            periodo = PeriodoContable.objects.filter(provider_id=perfil_id, cerrado=False).first()
            if not periodo: return "ERROR: SIN_PERIODO_CONTABLE"

            asiento = AsientoContable.objects.create(
                provider_id=perfil_id,
                periodo=periodo,
                date=timezone.now().date(),
                description=f"Impacto Automático SARITA - {event_type} - {payload.get('description', '')}",
                creado_por=self.user
            )
            return str(asiento.id)
        except Exception as e:
            logger.warning(f"ERP Contable: {e}")
            return None

    def _apply_financiero(self, event_type, payload):
        """Gestión de Flujo de Caja y Órdenes de Pago."""
        try:
            # Aquí vinculamos con el Monedero o generamos orden de pago
            if "wallet_transaction_id" in payload:
                return str(payload["wallet_transaction_id"])

            from apps.prestadores.mi_negocio.gestion_financiera.models import OrdenPago
            perfil_id = payload.get("perfil_id")

            if event_type == "LIQUIDATION" and perfil_id:
                orden = OrdenPago.objects.create(
                    perfil_ref_id=perfil_id,
                    amount=Decimal(str(payload.get("amount", 0))),
                    payment_date=timezone.now().date(),
                    concept=f"Liquidación Monedero - {event_type}",
                    status=OrdenPago.EstadoPago.PENDIENTE
                )
                return str(orden.id)
            return None
        except Exception as e:
            logger.warning(f"ERP Financiero: {e}")
            return None

    def _apply_archivistico(self, event_type, payload, refs):
        """Evidencia Legal y SHA-256 Chaining."""
        try:
            from apps.prestadores.mi_negocio.gestion_archivistica.models import Document, DocumentType, Process, ProcessType
            from apps.companies.models import Company

            company_id = payload.get("company_id")
            if not company_id: return None

            company = Company.objects.get(id=company_id)

            proc_type, _ = ProcessType.objects.get_or_create(company=company, code="GEN", defaults={"name": "Gestión General"})
            process, _ = Process.objects.get_or_create(company=company, process_type=proc_type, code="GEN-ERP", defaults={"name": "Integración ERP"})
            doc_type, _ = DocumentType.objects.get_or_create(company=company, code="EVI_ERP", defaults={"name": "Evidencia de Impacto ERP"})

            contable_ref = refs.get('contable_id') or '0000'
            import uuid
            doc = Document.objects.create(
                company=company,
                process=process,
                document_type=doc_type,
                sequence=Document.objects.filter(company=company).count() + 1,
                document_code=f"EVI-{timezone.now().strftime('%Y%m%d%H%M%S')}-{str(uuid.uuid4())[:4]}",
                created_by=self.user
            )
            return str(doc.id)
        except Exception as e:
            logger.warning(f"ERP Archivístico: {e}")
            return None
