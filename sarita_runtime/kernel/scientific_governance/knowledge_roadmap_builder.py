class KnowledgeRoadmapBuilder:
    def build_roadmap(self, plans):
        # Builds a sequential roadmap for knowledge expansion
        roadmap = []
        for i, plan in enumerate(plans):
            roadmap.append({"step": i+1, "action": f"EXPAND_{plan['domain']}"})
        return roadmap
