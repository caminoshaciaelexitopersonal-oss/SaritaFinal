class CausalErrorDetector:
    def detect_spurious_link(self, current_model, conflict_evidence):
        for link in current_model.get("links", []):
            if link["id"] == conflict_evidence.get("link_id") and conflict_evidence.get("refutation"):
                return link
        return None
