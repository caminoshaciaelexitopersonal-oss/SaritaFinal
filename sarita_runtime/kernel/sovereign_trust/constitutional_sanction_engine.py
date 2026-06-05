from sarita_runtime.kernel.constitutional_court.constitutional_court import ConstitutionalCase

class ConstitutionalSanctionEngine:
    """
    Engine to authorize and apply sanctions against rogue components (Phase 83.5).
    """
    def __init__(self, court, revocation_registry):
        self.court = court
        self.revocation_registry = revocation_registry

    def revoke_identity(self, subject_id: str, justification: str):
        case = ConstitutionalCase(subject_id, "REVOCATION", {"justification": justification})
        verdict = self.court.judge_case(case)

        if verdict.decision == "APPROVED":
            self.revocation_registry.revoke(subject_id, justification)
            return True
        return False
