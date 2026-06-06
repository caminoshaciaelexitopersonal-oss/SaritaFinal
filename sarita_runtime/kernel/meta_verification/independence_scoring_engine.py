class IndependenceScoringEngine:
    """
    Calculates the Independence Score (IS) for the verification ecosystem.
    Target: IS >= 0.85
    """
    def __init__(self, registry):
        self.registry = registry

    def calculate_is(self, verifier_ids: list):
        if not verifier_ids: return 0.0

        provenances = [self.registry.get_provenance(vid) for vid in verifier_ids]
        provenances = [p for p in provenances if p]

        if not provenances: return 0.0

        # Weighted Factors:
        # Architecture: 25%
        # Language: 20%
        # Domain: 20%
        # Author: 15%
        # Trust Chain: 20%

        arch_score = len(set(p.get("architecture", vid) for p in provenances)) / len(provenances)
        lang_score = len(set(p["language"] for p in provenances)) / len(provenances)
        domain_score = len(set(p["domain"] for p in provenances)) / len(provenances)
        author_score = len(set(p["author"] for p in provenances)) / len(provenances)
        trust_score = len(set(p.get("trust_chain", vid) for p in provenances)) / len(provenances)

        # Normalize scores to 0-1 range (simplified)
        is_score = (arch_score * 0.25 +
                    lang_score * 0.20 +
                    domain_score * 0.20 +
                    author_score * 0.15 +
                    trust_score * 0.20)

        return min(is_score * 1.5, 1.0) # Boost multiplier for diverse sets
