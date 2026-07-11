class DoubleBlindManager:
    """
    Anonymizes both subjects (runs) and reviewers to achieve full Double-Blind verification.
    """
    def __init__(self, reviewers: list):
        self.reviewers = reviewers

    def conduct_double_blind_review(self, raw_protocols: list) -> list:
        results = []
        for proto in raw_protocols:
            anonymized = {
                "sample_size": proto.get("sample_size"),
                "has_control_group": proto.get("has_control_group"),
                "has_hypothesis": proto.get("has_hypothesis")
            }

            reviewer_reports = []
            for rev in self.reviewers:
                report = rev.review_anonymized_protocol(anonymized)
                reviewer_reports.append(report)

            avg_score = sum(r["methodology_score"] for r in reviewer_reports) / len(reviewer_reports) if reviewer_reports else 0.0

            results.append({
                "original_protocol_id": proto.get("protocol_id"),
                "blinded_reviews_count": len(reviewer_reports),
                "consensus_methodology_score": round(avg_score, 4),
                "decision": "APPROVED" if avg_score >= 0.75 else "REJECTED"
            })
        return results
