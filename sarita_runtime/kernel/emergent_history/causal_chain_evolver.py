class CausalChainEvolver:
    def __init__(self):
        self.chains = {} # civ_id -> list of events

    def add_event(self, civ_id, event):
        if civ_id not in self.chains:
            self.chains[civ_id] = []
        self.chains[civ_id].append(event)

    def get_lineage(self, civ_id):
        return self.chains.get(civ_id, [])

    def link_events(self, event_a, event_b):
        # Symbolic linking of events to form causal narratives
        return f"{event_a} -> led to -> {event_b}"
