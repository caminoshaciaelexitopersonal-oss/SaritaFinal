class EvidenceConflictAnalyzer:
    def __init__(self):
        self.conflicts = []

    def analyze(self, belief, new_evidence):
        old_evidence_strength = belief.get("evidence_strength", 0.5)
        new_evidence_strength = new_evidence.get("strength", 0.5)

        if new_evidence.get("supports") is False and new_evidence_strength > old_evidence_strength:
            conflict = {
                "belief_id": belief.get("id"),
                "conflict_severity": new_evidence_strength - old_evidence_strength,
                "recommendation": "REVISE"
            }
            self.conflicts.append(conflict)
            return conflict
        return None
