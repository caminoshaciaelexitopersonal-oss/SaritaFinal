class PhysicalExecutionVertex:
    def __init__(self, task_id, payload):
        self.task_id = task_id
        self.payload = payload
        self.edges = []
