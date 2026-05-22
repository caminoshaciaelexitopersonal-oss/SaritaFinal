import logging

class ExecutionBlastRadiusController:
    """
    Failure Containment Fabric.
    Automatically isolates poisoned runtimes to prevent cascade failure.
    """
    def __init__(self):
        self.quarantined_nodes = set()

    def quarantine_node(self, node_id, reason):
        logging.error(f"Containment Fabric: QUARANTINING node {node_id}. Reason: {reason}")
        self.quarantined_nodes.add(node_id)

    def is_isolated(self, node_id):
        return node_id in self.quarantined_nodes

class RuntimeCircuitBreaker:
    def __init__(self, failure_threshold=5):
        self.failures = 0
        self.threshold = failure_threshold
        self.state = "CLOSED"

    def record_failure(self):
        self.failures += 1
        if self.failures >= self.threshold:
            self.state = "OPEN"
            logging.warning("Circuit Breaker: Runtime execution halted for containment.")
