class SovereignCertificationCalculator:
    """
    Computes GSCI based on:
    - EA: Evolution Authenticity
    - CT: Causal Traceability
    - MR: Mathematical Rigor
    - SC: Scientific Reproducibility
    - CI: Constitutional Integrity
    - EQ: Evidence Quality
    """
    def compute_gsci(self, metrics):
        weights = {
            "evolution_authenticity": 0.20,
            "causal_traceability": 0.20,
            "mathematical_rigor": 0.15,
            "scientific_reproducibility": 0.15,
            "constitutional_integrity": 0.15,
            "evidence_quality": 0.15
        }

        gsci_score = 0.0
        for key, weight in weights.items():
            gsci_score += metrics.get(key, 0.0) * weight

        return {
            "gsci_score": round(gsci_score, 4),
            "submetrics": metrics,
            "certification_level": "SOVEREIGN_SCIENTIFIC_PLATINUM" if gsci_score >= 0.98 else "GOLD"
        }
