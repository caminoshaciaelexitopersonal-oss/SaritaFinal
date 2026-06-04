from typing import Any

class HardwareObservabilityEngine:
    def __init__(self, recorder):
        self.recorder = recorder
    def observe_transition(self, resource_type: str, resource_id: Any, before: Any, expected: Any, actual: Any):
        match = (expected == actual)
        self.recorder.record_action(f"OBSERVE_{resource_type.upper()}", str(resource_id), {"before": str(before), "expected": str(expected), "actual": str(actual)}, "CONSISTENT" if match else "DIVERGENT")
        return match
