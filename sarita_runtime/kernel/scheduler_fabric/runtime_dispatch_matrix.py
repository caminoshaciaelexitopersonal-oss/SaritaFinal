import logging

class RuntimeDispatchMatrix:
    """
    Physical dispatch matrix. Maps causal vertices to persistent workers.
    """
    def __init__(self):
        self.matrix = {}

    def assign_dispatch(self, vertex_id: str, worker_id: str):
        logging.info(f"Dispatch Matrix: Assigning {vertex_id} -> {worker_id}")
        self.matrix[vertex_id] = worker_id
