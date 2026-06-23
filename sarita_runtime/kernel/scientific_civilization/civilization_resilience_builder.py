class CivilizationResilienceBuilder:
    def build_resilience(self, stability_score):
        # Strengthens redundancy if stability is low
        return {"redundancy_level": "HIGH" if stability_score < 0.5 else "NORMAL"}
