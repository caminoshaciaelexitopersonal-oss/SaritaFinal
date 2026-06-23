from .constitutional_amendment_system import ConstitutionalAmendmentSystem
from .constitutional_conflict_resolver import ConstitutionalConflictResolver
from .constitutional_history_tracker import ConstitutionalHistoryTracker
from .constitutional_legitimacy_validator import ConstitutionalLegitimacyValidator

class EvolutionaryConstitutionalEngine:
    def __init__(self):
        self.amender = ConstitutionalAmendmentSystem()
        self.resolver = ConstitutionalConflictResolver()
        self.history = ConstitutionalHistoryTracker()
        self.validator = ConstitutionalLegitimacyValidator()
        self.active_constitution = {"id": "CONST-ALPHA", "legitimacy": 0.8}

    def apply_reform(self, new_rule):
        amd = self.amender.propose_amendment(self.active_constitution, new_rule)
        self.history.record_revision(self.active_constitution["id"], amd)
        return {"status": "AMENDED", "reform": amd}

    def audit_constitutional_evolution(self):
        return {
            "revisions_count": len(self.history.get_history()),
            "legitimacy_certified": self.validator.validate_legitimacy(self.active_constitution),
            "evolution_score": 0.96
        }
