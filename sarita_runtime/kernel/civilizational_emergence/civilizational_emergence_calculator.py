class CivilizationalEmergenceCalculator:
    def calculate_gcei(self, metrics):
        ia = metrics.get("institutional_autonomy", 0.0)
        sp = metrics.get("scientific_pluralism", 0.0)
        hs = metrics.get("historical_stability", 0.0)
        gc = metrics.get("generational_continuity", 0.0)
        ci = metrics.get("constitutional_independence", 0.0)
        ir = metrics.get("institutional_resilience", 0.0)

        gcei = (ia + sp + hs + gc + ci + ir) / 6.0
        return max(0.0000, min(1.0000, gcei))
