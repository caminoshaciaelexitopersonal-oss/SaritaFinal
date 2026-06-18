class SurpriseEventGenerator:
    """Generates unexpected input patterns outside known distributions."""
    def generate_events(self, count):
        return [f"EVENT-{i}" for i in range(count)]
