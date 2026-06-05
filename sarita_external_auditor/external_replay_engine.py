import json

class ExternalReplayEngine:
    """
    Reconstructs state transformations from exported event logs (Phase 87.3).
    """
    def __init__(self):
        self.state = {
            "ownership": {},
            "pressure": 0.0,
            "vertices": []
        }

    def process_event_log(self, event_log: list):
        for event in event_log:
            action = event.get('action')
            payload = event.get('payload', {})

            if action == "OWNERSHIP_CHANGE":
                self.state["ownership"][payload['resource']] = payload['owner']
            elif action == "PRESSURE_UPDATE":
                self.state["pressure"] = payload.get('score', 0.0)

            self.state["vertices"].append(event.get('vertex_id'))

        return self.state

class ExternalStateRebuilder:
    """Independent engine to rebuild and certify state snapshots."""
    def rebuild_from_evidence(self, initial_state, events):
        engine = ExternalReplayEngine()
        engine.state = initial_state
        return engine.process_event_log(events)
