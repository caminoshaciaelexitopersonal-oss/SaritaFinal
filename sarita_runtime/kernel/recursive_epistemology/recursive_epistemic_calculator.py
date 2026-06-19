class RecursiveEpistemicCalculator:
    def calculate_gresi(self, metrics):
        rv = metrics.get("recursive_validation", 0.0)
        mf = metrics.get("meta_falsifiability", 0.0)
        pd = metrics.get("paradigm_diversity", 0.0)
        fr = metrics.get("fossilization_resistance", 0.0)
        rc = metrics.get("recursive_confidence", 0.0)
        lg = metrics.get("learning_governance", 0.0)

        gresi = (rv * 0.20 + mf * 0.20 + pd * 0.15 + fr * 0.15 + rc * 0.15 + lg * 0.15)
        return max(0.0000, min(1.0000, gresi))
