class ParadigmConflictDetector:
    def detect_conflict(self, current_paradigm, new_evidence_set):
        # A paradigm shift is triggered when cumulative evidence against the current paradigm
        # exceeds its foundational stability
        anomaly_count = sum(1 for e in new_evidence_set if e.get("anomalous") is True)
        if anomaly_count > current_paradigm.get("anomaly_threshold", 10):
            return {
                "paradigm_id": current_paradigm.get("id"),
                "status": "CONFLICT",
                "anomaly_count": anomaly_count
            }
        return None
