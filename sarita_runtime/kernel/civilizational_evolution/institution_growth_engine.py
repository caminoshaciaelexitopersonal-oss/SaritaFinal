class InstitutionGrowthEngine:
    def evolve(self, institution, resources_available):
        growth_factor = institution["fitness"] * resources_available
        institution["resources"] += growth_factor
        institution["fitness"] = min(1.0, institution["fitness"] + 0.01)
        institution["status"] = "GROWTH"
        return institution
