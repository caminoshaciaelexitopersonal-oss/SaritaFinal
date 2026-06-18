class EpistemicSelfCorrectionCalculator:
    def calculate_gesi(self, metrics):
        br = metrics.get("belief_revision", 0.0)
        ps = metrics.get("paradigm_shift", 0.0)
        cr = metrics.get("causal_revision", 0.0)
        el = metrics.get("error_learning", 0.0)
        rc = metrics.get("recalibrated_confidence", 0.0)
        fa = metrics.get("falsifiability_assurance", 0.0)

        # Weighted average for GESI
        gesi = (br * 0.15 + ps * 0.20 + cr * 0.15 + el * 0.20 + rc * 0.15 + fa * 0.15)
        return max(0.0000, min(1.0000, gesi))
