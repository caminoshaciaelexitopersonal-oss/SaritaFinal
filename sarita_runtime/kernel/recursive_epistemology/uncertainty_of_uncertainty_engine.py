class UncertaintyOfUncertaintyEngine:
    def calculate_meta_uncertainty(self, uncertainty_sigma, evidence_variance):
        # Measures uncertainty about the system's own uncertainty estimate
        return abs(uncertainty_sigma - evidence_variance)
