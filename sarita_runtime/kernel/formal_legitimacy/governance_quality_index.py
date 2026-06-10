class GovernanceQualityIndex:
    """
    Quantifies the quality of autonomous governance decisions.
    """

    def calculate_gqi(self,
                      decision_latency: float,
                      recovery_success_rate: float,
                      audit_coverage: float) -> float:
        """
        GQI = (SuccessRate * AuditCoverage) / (1 + Latency)
        Normalized to [0, 1]
        """
        raw_gqi = (recovery_success_rate * audit_coverage) / (1.0 + decision_latency)
        return float(round(max(0.0, min(1.0, raw_gqi)), 4))
