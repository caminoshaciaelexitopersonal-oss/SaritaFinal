import logging
from decimal import Decimal
from typing import List, Dict, Any
from django.db import models
from django.utils import timezone
from .models import Jurisdiction, TaxRule, TaxAuditTrail

logger = logging.getLogger(__name__)

class TaxEngine:
    """
    Motor Fiscal Global del Core ERP.
    Soporta múltiples jurisdicciones, reglas versionables y auditoría total.
    """

    @staticmethod
    def calculate_taxes(transaction_payload: Dict[str, Any]) -> List[Dict[str, Any]]:
        """
        Calcula impuestos aplicables a una transacción basada en su jurisdicción.
        """
        # 1. Resolver Jurisdicción
        country_code = transaction_payload.get('country_code', 'CO') # Default CO
        jurisdiction = Jurisdiction.objects.filter(country_code=country_code, is_active=True).first()

        if not jurisdiction:
            logger.warning(f"No active jurisdiction found for country {country_code}. Using fallback empty taxes.")
            return []

        # 2. Cargar Reglas Vigentes
        now = timezone.now().date()
        rules = TaxRule.objects.filter(
            jurisdiction=jurisdiction,
            effective_from__lte=now,
            is_active=True
        ).filter(models.Q(effective_to__isnull=True) | models.Q(effective_to__gte=now))

        tax_breakdown = []
        base_amount = Decimal(str(transaction_payload.get('amount', 0)))
        reference = transaction_payload.get('reference', 'N/A')

        for rule in rules:
            # 3. Calcular Impuesto
            # Aquí se puede añadir lógica más compleja por tipo de impuesto
            tax_amount = (base_amount * rule.rate).quantize(Decimal('0.01'))

            tax_entry = {
                'tax_rule_id': str(rule.id),
                'tax_name': rule.name,
                'tax_type': rule.tax_type,
                'rate': float(rule.rate),
                'tax_amount': tax_amount,
                'version': rule.version
            }
            tax_breakdown.append(tax_entry)

            # 4. Auditoría Fiscal (Fase 7 - II.7)
            TaxAuditTrail.objects.create(
                transaction_reference=reference,
                jurisdiction=jurisdiction,
                rule_applied=rule,
                base_amount=base_amount,
                tax_amount=tax_amount,
                calculation_path={
                    'engine': 'TaxEngineGlobal',
                    'timestamp': timezone.now().isoformat(),
                    'method': 'rate_multiplier'
                }
            )

        return tax_breakdown

    @staticmethod
    def get_regulatory_deadlines(jurisdiction_id: str):
        """
        Retorna fechas límite próximas para una jurisdicción.
        """
        from .models import RegulatoryCalendar
        return RegulatoryCalendar.objects.filter(jurisdiction_id=jurisdiction_id)
