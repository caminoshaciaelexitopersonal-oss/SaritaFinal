class ArchitectureLineageTracker:
    def __init__(self):
        self.lineage = {}

    def register(self, architecture):
        aid = architecture["identity"]["id"]
        pid = architecture["identity"]["parent_id"]
        self.lineage[aid] = {
            "parent": pid,
            "generation": architecture["generation"],
            "children": []
        }
        if pid and pid in self.lineage:
            self.lineage[pid]["children"].append(aid)

    def get_genealogy(self, aid):
        genealogy = []
        current = aid
        while current:
            genealogy.append(current)
            current = self.lineage.get(current, {}).get("parent")
        return genealogy
