import time
import uuid

class ConstitutionalCase:
    def __init__(self, subject: str, action: str, details: dict):
        self.case_id = str(uuid.uuid4())
        self.subject = subject
        self.action = action
        self.details = details
        self.timestamp = time.time()

class ConstitutionalVerdict:
    def __init__(self, case_id: str, decision: str, justification: str):
        self.case_id = case_id
        self.decision = decision # "APPROVED" or "REJECTED"
        self.justification = justification
        self.issued_at = time.time()

class ConstitutionalCourt:
    """
    Independent tribunal for kernel structural and authority decisions (Phase 82.3/83.5).
    """
    def __init__(self, identity_engine, revocation_registry=None):
        self.identity_engine = identity_engine
        self.revocation_registry = revocation_registry
        self.cases = []
        self.verdicts = []

    def judge_case(self, case: ConstitutionalCase):
        self.cases.append(case)

        # 1. Check Revocation Status (Phase 83.5)
        if self.revocation_registry and not self.revocation_registry.is_valid(case.subject):
            verdict = ConstitutionalVerdict(case.case_id, "REJECTED", f"Identity for '{case.subject}' is REVOKED or QUARANTINED.")
            self.verdicts.append(verdict)
            return verdict

        # 2. Judge Action
        if case.action == "MUTATE_STATE":
            is_valid = self.identity_engine.validate_identity(case.subject, case.details.get('file_path'))
            if is_valid:
                verdict = ConstitutionalVerdict(case.case_id, "APPROVED", "Identity verified cryptographically.")
            else:
                verdict = ConstitutionalVerdict(case.case_id, "REJECTED", "Unauthorized component identity.")
        elif case.action in ["REVOCATION", "QUARANTINE", "SUSPENSION"]:
            # Sanction logic
            verdict = ConstitutionalVerdict(case.case_id, "APPROVED", "Sanction authorized by Judicial Precedent.")
        else:
            verdict = ConstitutionalVerdict(case.case_id, "REJECTED", "Unknown action.")

        self.verdicts.append(verdict)
        return verdict
