import copy

class ExecutionSnapshot:
    """
    Records deep memory copies of active datasets and indices.
    """
    def __init__(self):
        self.snapshots = {}

    def capture_snapshot(self, snapshot_id: str, data: dict):
        self.snapshots[snapshot_id] = copy.deepcopy(data)

    def retrieve_snapshot(self, snapshot_id: str) -> dict:
        return self.snapshots.get(snapshot_id, {})
