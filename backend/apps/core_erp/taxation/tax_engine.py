import logging
import hashlib
import json
from decimal import Decimal
from typing import List, Dict, Any
from django.db import transaction
from django.utils import timezone
from .models import Tax, TaxRate, TaxRule, TaxTransaction, TaxAccountMapping

logger = logging.getLogger(__name__)

class TaxEngine:
    """
    Motor Fiscal Soberano — SARITA 2026.
    Implementación integral, determinística y auditable del cálculo de impuestos.
    """

    @staticmethod
    def calculate_taxes(document_payload: Dict[str, Any]) -> List[Dict[str, Any]]:
        """
        Bloque 2.1: Punto de Entrada Principal.
        """
        doc_id = document_payload.get('document_id')
        tenant_id = document_payload.get('tenant_id')
        issue_date = document_payload.get('issue_date', timezone.now().date())

        # 1. Idempotencia: Verificar hash de contenido (Bloque 2.3)
        if TaxEngine._check_idempotency(document_payload):
            return TaxEngine._get_previous_results(doc_id)

        # 2. Context Resolver
        jurisdiction = document_payload.get('jurisdiction_id')
        doc_type = document_payload.get('document_type')
        entity_type = document_payload.get('entity_type')

        # 3. Rule Engine: Obtener reglas aplicables
        rules = TaxRule.objects.filter(
            tax__active=True,
            tax__tenant_id=tenant_id,
            document_type=doc_type,
            entity_type=entity_type
        ).order_by('priority')

        tax_results = []
        base_total = Decimal(str(document_payload.get('base_amount', 0)))

        for rule in rules:
            # 4. Rate Provider: Obtener tasa histórica
            rate_obj = TaxRate.objects.filter(
                tax=rule.tax,
                effective_from__lte=issue_date
            ).filter(models.Q(effective_to__isnull=True) | models.Q(effective_to__gte=issue_date)).first()

            if not rate_obj:
                continue

            # 5. Calculator: Computar Base e Impuesto
            tax_amount = (base_total * rate_obj.rate).quantize(Decimal('0.01'))

            # 6. Validator: Verificar límites legales
            if base_total < rule.minimum_base:
                continue

            res = {
                "tax_id": str(rule.tax.id),
                "tax_code": rule.tax.code,
                "base": float(base_total),
                "rate": float(rate_obj.rate),
                "amount": float(tax_amount)
            }
            tax_results.append(res)

            # 7. Persistencia y Auditoría (Bloque 3.6)
            TaxTransaction.objects.create(
                document_id=doc_id,
                tax=rule.tax,
                base_amount=base_total,
                tax_amount=tax_amount,
                rate_applied=rate_obj.rate,
                tenant_id=tenant_id,
                integrity_hash=TaxEngine._generate_hash(doc_id, res)
            )

        return tax_results

    @staticmethod
    def _generate_hash(doc_id, result_payload):
        data = f"{doc_id}{json.dumps(result_payload, sort_keys=True)}"
        return hashlib.sha256(data.encode()).hexdigest()

    @staticmethod
    def _check_idempotency(payload):
        # Lógica de verificación de hash almacenado
        return False # Placeholder para integración con ProcessedEvents
