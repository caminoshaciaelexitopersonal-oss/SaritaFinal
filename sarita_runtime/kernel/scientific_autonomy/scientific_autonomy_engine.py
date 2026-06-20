from .autonomous_discovery_validator import AutonomousDiscoveryValidator
from .knowledge_creation_certifier import KnowledgeCreationCertifier
from .independent_reasoning_auditor import IndependentReasoningAuditor

class ScientificAutonomyEngine:
    def __init__(self):
        self.validator = AutonomousDiscoveryValidator()
        self.certifier = KnowledgeCreationCertifier()
        self.auditor = IndependentReasoningAuditor()

    def certify_autonomy(self, discovery_record):
        is_valid = self.validator.validate_discovery(discovery_record)
        audit = self.auditor.audit_reasoning(discovery_record)
        certification = self.certifier.certify_knowledge(discovery_record, is_valid)

        return {
            "valid": is_valid,
            "independent": audit["independent"],
            "certification": certification
        }
