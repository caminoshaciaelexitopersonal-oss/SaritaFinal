class CertaintyReassessmentEngine:
    def reassess(self, current_confidence, new_anomalies_count):
        # Certainty drops sharply as anomalies accumulate
        reassessed = current_confidence / (1.0 + new_anomalies_count)
        return max(0.0, min(1.0, reassessed))
