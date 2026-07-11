class ConsensusBuilder:
    """
    Builds statistical and logical consensus between multiple independent review reports or replication outcomes.
    """
    def __init__(self):
        pass

    def build_consensus_verdict(self, review_reports: list) -> dict:
        if not review_reports:
            return {"verdict": "NO_REPORTS", "consensus_score": 0.0}

        accept_count = sum(1 for r in review_reports if r.get("recommendation") == "ACCEPT")
        total = len(review_reports)
        ratio = accept_count / total

        if ratio >= 0.7:
            verdict = "ACCEPTED_BY_CONSENSUS"
        elif ratio >= 0.4:
            verdict = "REQUIRES_REVISION"
        else:
            verdict = "REJECTED_BY_CONSENSUS"

        return {
            "verdict": verdict,
            "consensus_score": round(ratio, 4),
            "total_reviews": total,
            "approvals": accept_count
        }
