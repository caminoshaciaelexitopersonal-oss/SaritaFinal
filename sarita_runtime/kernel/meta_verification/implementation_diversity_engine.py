class ImplementationDiversityEngine:
    """
    Calculates the Implementation Diversity Score (IDS) for a set of verifiers.
    Target: IDS >= 0.70
    """
    def __init__(self, provenance_registry):
        self.registry = provenance_registry

    def calculate_ids(self, verifier_ids: list):
        if not verifier_ids: return 0.0

        provenances = [self.registry.get_provenance(vid) for vid in verifier_ids]
        provenances = [p for p in provenances if p]

        if not provenances: return 0.0

        total_verifiers = len(provenances)

        # 1. Language Diversity
        languages = set(p["language"] for p in provenances)
        lang_score = len(languages) / total_verifiers

        # 2. Implementation Diversity
        impls = set(p["implementation"] for p in provenances)
        impl_score = len(impls) / total_verifiers

        # 3. Domain Diversity
        domains = set(p["domain"] for p in provenances)
        domain_score = len(domains) / total_verifiers

        # IDS is the average of these scores
        ids = (lang_score + impl_score + domain_score) / 3.0
        return ids
