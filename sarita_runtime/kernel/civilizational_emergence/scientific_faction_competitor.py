class ScientificFactionCompetitor:
    def run_faction_competition(self, factions, evidence):
        # Factions compete for evidence support
        for f in factions.values():
            f["support"] = f.get("support", 0.5) * 1.02 # Simple growth
        return sorted(factions.values(), key=lambda x: x["support"], reverse=True)
