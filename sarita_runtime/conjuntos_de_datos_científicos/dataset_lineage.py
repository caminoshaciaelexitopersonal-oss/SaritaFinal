class DatasetLineage:
    """
    Maintains a parent-child genealogy of derivative scientific datasets and traces their origin source hashes.
    """
    def __init__(self):
        self.lineage = {}

    def record_lineage(self, child_id: str, parent_id: str):
        self.lineage[child_id] = parent_id

    def trace_lineage(self, child_id: str) -> list:
        path = []
        curr = child_id
        while curr:
            path.append(curr)
            curr = self.lineage.get(curr)
        return path
