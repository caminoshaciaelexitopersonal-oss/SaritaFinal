class AuditorLineageTracker:
    """
    Tracks the genealogical relationship between different auditors.
    Detects if an auditor is a derivative or clone of another.
    """
    def __init__(self):
        self.lineage = {} # child_id -> parent_id

    def add_lineage(self, child_id: str, parent_id: str = None):
        self.lineage[child_id] = parent_id

    def get_ancestry(self, auditor_id: str):
        ancestry = []
        curr = auditor_id
        while curr in self.lineage and self.lineage[curr]:
            ancestry.append(self.lineage[curr])
            curr = self.lineage[curr]
        return ancestry

    def are_related(self, id1: str, id2: str):
        anc1 = set(self.get_ancestry(id1)) | {id1}
        anc2 = set(self.get_ancestry(id2)) | {id2}
        return not anc1.isdisjoint(anc2)
