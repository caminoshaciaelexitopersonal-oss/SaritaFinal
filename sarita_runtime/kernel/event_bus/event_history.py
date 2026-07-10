import json
import os

class EventHistory:
    """
    Handles persistence and historical query indexing of system-wide events.
    """
    def __init__(self):
        self.history_file = "sarita_runtime/kernel/event_bus/event_history.json"
        self.events = []
        self.load_history()

    def load_history(self):
        if os.path.exists(self.history_file):
            try:
                with open(self.history_file, "r") as f:
                    self.events = json.load(f)
            except Exception:
                pass

    def record_event(self, event):
        self.events.append(event)
        # Limit to 1000 items to keep file sizes clean
        if len(self.events) > 1000:
            self.events = self.events[-1000:]
        self.save_history()

    def save_history(self):
        os.makedirs(os.path.dirname(self.history_file), exist_ok=True)
        with open(self.history_file, "w") as f:
            json.dump(self.events, f, indent=2)

    def query(self, filters: dict) -> list:
        res = self.events
        for key, val in filters.items():
            res = [e for e in res if e.get(key) == val]
        return res
