import logging

class PhysicalResourceLineage:
    """
    Tracks absolute physical ownership history.
    """
    def __init__(self):
        self.history = []

    def record_ownership_change(self, resource_id: str, old_owner: str, new_owner: str):
        logging.info(f"Resource Lineage: {resource_id} migrated {old_owner} -> {new_owner}")
        self.history.append({"res": resource_id, "from": old_owner, "to": new_owner})
