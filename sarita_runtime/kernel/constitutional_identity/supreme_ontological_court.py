class SupremeOntologicalCourt:
    """
    The supreme tribunal for all identity and ontological decisions.
    """
    def __init__(self, adjudicator, reviewer, validator):
        self.adjudicator = adjudicator
        self.reviewer = reviewer
        self.validator = validator

    def judge_evolutionary_identity(self, reform: dict, is_integral: bool):
        # 1. Review essence
        essence_ok, essence_msg = self.reviewer.review_essence(reform)

        # 2. Adjudicate
        identity_ok, identity_msg = self.adjudicator.adjudicate_identity(reform, is_integral)

        verdict = essence_ok and identity_ok

        return {
            "verdict": "APPROVED" if verdict else "REJECTED",
            "essence_report": essence_msg,
            "identity_report": identity_msg,
            "ontological_integrity": verdict
        }
