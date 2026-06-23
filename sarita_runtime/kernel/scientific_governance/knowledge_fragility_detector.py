class KnowledgeFragilityDetector:
    def detect_fragility(self, theory):
        # Theory is fragile if its validity depends on a single evidence source
        return 1.0 / max(1, theory.get("evidence_sources_count", 1))
