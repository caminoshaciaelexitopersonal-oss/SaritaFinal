import logging

class RegisteredBufferLineage:
    """
    Tracks lineage of physical registered buffers.
    Ensures zero-copy IO follows causal vertices.
    """
    def __init__(self):
        self.buffer_owners = {}

    def assign_buffer(self, buffer_id: str, task_id: str):
        logging.info(f"Buffer Lineage: Buffer {buffer_id} assigned to {task_id}")
        self.buffer_owners[buffer_id] = task_id
