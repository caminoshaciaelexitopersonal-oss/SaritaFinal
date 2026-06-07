import time

class ConstitutionalSelfReview:
    """
    Executes periodic internal reviews of the kernel's constitutional state.
    """
    def __init__(self, ledger):
        self.ledger = ledger

    def perform_review(self):
        # Review last 100 decisions
        decisions = self.ledger.get_history()[-100:]
        violations = [d for d in decisions if d.get("status") == "violation"]

        report = {
            "timestamp": time.time(),
            "reviewed_count": len(decisions),
            "violation_rate": len(violations) / len(decisions) if decisions else 0,
            "status": "HEALTHY" if len(violations) < 2 else "RISK"
        }
        return report
