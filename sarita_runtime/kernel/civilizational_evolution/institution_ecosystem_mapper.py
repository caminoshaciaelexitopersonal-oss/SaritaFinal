class InstitutionEcosystemMapper:
    def map_relationships(self, institutions):
        mapping = {}
        for inst in institutions:
            mapping[inst["id"]] = inst.get("alliances", [])
        return mapping
