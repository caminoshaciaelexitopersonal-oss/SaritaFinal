class SuperordinateCognitionTracker:
    def __init__(self):
        self.super_cognitive_events = []

    def track_event(self, event_type, power):
        self.super_cognitive_events.append({
            "type": event_type,
            "power": power
        })
