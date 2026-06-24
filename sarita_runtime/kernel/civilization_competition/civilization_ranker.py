class CivilizationRanker:
    def rank_civilizations(self, civilizations, resource_manager, innovation_engine):
        scored_civs = []
        for civ in civilizations:
            civ_id = civ["identity"]["id"]
            resources = resource_manager.get_resources(civ_id)
            innovation = innovation_engine.innovation_levels.get(civ_id, 0)

            score = (resources * 0.4) + (innovation * 100 * 0.6)
            scored_civs.append((civ, score))

        return sorted(scored_civs, key=lambda x: x[1], reverse=True)
