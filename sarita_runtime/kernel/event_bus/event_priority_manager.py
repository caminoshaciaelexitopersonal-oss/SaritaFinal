class EventPriorityManager:
    """
    Manages prioritization levels for events in the system.
    Critical errors and attacks bypass queues and get immediately processed.
    """
    def __init__(self):
        self.priorities = {
            "security.attack_detected": 10,
            "axiom.violation": 9,
            "health.alert": 8,
            "system.shutdown": 8,
            "system.boot": 7,
            "decision.made": 5,
            "state.changed": 4,
            "metric.updated": 3,
            "knowledge.mutated": 3
        }

    def get_priority(self, event_type: str) -> int:
        return self.priorities.get(event_type, 1) # Default standard priority
