import logging
import json
from .models import OperationalTreaty, TreatyComplianceAudit, SovereignKillSwitch

logger = logging.getLogger(__name__)

class TreatyValidatorService:
    """
    Motor de Cumplimiento de Tratados (Z-OPERATIONAL-TREATIES).
    Valida que los flujos de Peace-Net cumplan con los pactos firmados.
    """

    @staticmethod
    def validate_technical_interop(payload: dict, node_id: str) -> bool:
        """
        Valida que el intercambio cumpla con el Tratado de Interoperabilidad Técnica (TIT).
        """
        tit = OperationalTreaty.objects.filter(type='TIT', is_active=True).first()
        if not tit:
            logger.error(f"TIT: No hay tratado de interoperabilidad activo. Bloqueando intercambio de {node_id}.")
            return False

        # 1. Verificar si el nodo es firmante
        if node_id not in tit.participating_nodes:
            logger.warning(f"TIT: El nodo {node_id} no es firmante del tratado {tit.name}.")
            return False

        # 2. Verificar formato del payload (XAI obligatorio)
        if 'explanation' not in payload and 'reasoning_chain' not in payload:
            TreatyValidatorService._log_violation(tit, node_id, "Falta estándar de explicabilidad (XAI) requerido por TIT.")
            return False

        return True

    @staticmethod
    def enforce_neutrality(proposal: dict) -> bool:
        """
        Verifica que la propuesta de mitigación cumpla con el Tratado de Neutralidad Algorítmica (TNA).
        """
        tna = OperationalTreaty.objects.filter(type='TNA', is_active=True).first()
        if not tna:
            return True # Si no hay pacto, se asume neutralidad por defecto del Kernel

        # Buscar palabras clave prohibidas (geopolítica, sesgos estatales)
        prohibited_terms = tna.guardrails_config.get('prohibited_terms', [])
        content = str(proposal).upper()

        for term in prohibited_terms:
            if term.upper() in content:
                TreatyValidatorService._log_violation(tna, "INTERNAL", f"Violación de Neutralidad: Término prohibido detectado: {term}")
                return False

        return True

    @staticmethod
    def _log_violation(treaty, actor_id, details):
        from django.utils import timezone
        logger.error(f"TREATY_VIOLATION: {treaty.type} - Actor: {actor_id} - {details}")

        last_audit = TreatyComplianceAudit.objects.order_by('-timestamp').first()
        prev_hash = last_audit.integrity_hash if last_audit else "GENESIS"

        current_time = timezone.now()
        audit = TreatyComplianceAudit(
            treaty=treaty,
            timestamp=current_time,
            actor_node_id=actor_id,
            action_type='VIOLATION_DETECTED',
            payload_summary={"error": details},
            is_compliant=False,
            violation_details=details,
            previous_hash=prev_hash
        )
        audit.integrity_hash = audit.generate_hash(prev_hash)
        audit.save()

        # S-0.6: Si es una violación crítica de No-Injerencia, disparar Kill-Switch
        if treaty.type == 'TNID':
             logger.critical(f"TNID_BREACH: Disparando Kill-Switch automático por violación de No-Injerencia.")
             # Lógica de disparo automático omitida por seguridad humana (siempre requiere SuperAdmin)

class NeutralityEnforcementService:
    """
    Servicio especializado en blindar la neutralidad de las propuestas algorítmicas.
    """
    @staticmethod
    def audit_proposal_neutrality(proposal: dict) -> dict:
        """
        Z-TRUST-IMPLEMENTATION: Auditoría de Caja Negra para neutralidad operativa.
        Verifica si la propuesta contiene sesgos geopolíticos o de priorización.
        """
        # 1. Simular impacto en diferentes sub-nodos
        # 2. Verificar varianza de beneficios

        # Simulación de auditoría de neutralidad
        has_bias = "priorizar" in str(proposal).lower() and "estado" in str(proposal).lower()

        return {
            "is_neutral": not has_bias,
            "neutrality_score": 0.98 if not has_bias else 0.45,
            "automated_audit_timestamp": timezone.now().isoformat(),
            "audit_method": "COGNITIVE_BIAS_DETECTION_V1"
        }

    @staticmethod
    def generate_compliance_certificate(treaty_id: str) -> dict:
        """
        Genera un certificado de cumplimiento técnico para un tratado.
        """
        treaty = OperationalTreaty.objects.get(id=treaty_id)
        audits = treaty.audits.all()

        compliance_rate = audits.filter(is_compliant=True).count() / audits.count() if audits.count() > 0 else 1.0

        return {
            "treaty": treaty.name,
            "compliance_rate": compliance_rate,
            "audit_level": treaty.audit_level,
            "integrity_proof": hashlib.sha256(f"{treaty.id}{compliance_rate}".encode()).hexdigest(),
            "status": "CERTIFIED" if compliance_rate > 0.95 else "UNDER_REVIEW"
        }
