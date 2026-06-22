class KnowledgeLifecycleManager:
    def determine_state(self, theory_age, evidence_strength):
        if theory_age < 100:
            return "DISCOVERY"
        if evidence_strength > 0.9:
            return "MATURATION"
        if evidence_strength < 0.3:
            return "OBSOLESCENCE"
        return "STABLE"
