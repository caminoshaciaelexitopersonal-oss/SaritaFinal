import uuid

class HistoricalPathGenerator:
    def __init__(self):
        pass

    def generate_path(self, event_type, participants):
        path_id = str(uuid.uuid4())[:8]
        return f"PATH-{path_id}: {event_type} involving {', '.join(participants)}"
