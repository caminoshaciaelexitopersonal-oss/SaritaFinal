class ConfidenceOfConfidenceCalculator:
    def calculate_meta_confidence(self, base_confidence, evidence_consistency):
        # High meta-confidence when base confidence matches evidence consistency
        return 1.0 - abs(base_confidence - evidence_consistency)
