import datetime

class ExperimentLifecycle:
    """
    Tracks and enforces state transitions for scientific experiments.
    """
    VALID_TRANSITIONS = {
        "CREATED": ["SCHEDULED", "RUNNING"],
        "SCHEDULED": ["RUNNING"],
        "RUNNING": ["COMPLETED", "FAILED"],
        "COMPLETED": ["VALIDATED", "ARCHIVED"],
        "FAILED": ["CREATED", "ARCHIVED"],
        "VALIDATED": ["ARCHIVED"],
        "ARCHIVED": []
    }

    def __init__(self):
        pass

    def transition(self, experiment, new_state: str):
        current_state = experiment.status
        if new_state in self.VALID_TRANSITIONS.get(current_state, []):
            experiment.status = new_state
            experiment.traceability_chain.append(
                f"Transitioned from {current_state} to {new_state} at {datetime.datetime.now(datetime.timezone.utc).isoformat()}"
            )
            return True
        else:
            raise ValueError(f"Invalid transition from {current_state} to {new_state}.")
