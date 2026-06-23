class InstitutionCompetitionEngine:
    def run_competition(self, institutions):
        # Institutions compete for "reputation" based on discovery quality
        for inst in institutions:
            inst["reputation"] = inst.get("reputation", 0.5) * 1.05 # Growth simulation
        return sorted(institutions, key=lambda x: x.get("reputation", 0), reverse=True)
