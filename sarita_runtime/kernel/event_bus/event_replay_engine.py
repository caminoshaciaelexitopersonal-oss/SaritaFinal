class EventReplayEngine:
    """
    Replays historical event streams to reconstruct system states or re-trigger handlers.
    """
    def __init__(self, event_bus):
        self.bus = event_bus

    def replay_range(self, start_idx: int, end_idx: int) -> int:
        events = self.bus.history.events[start_idx:end_idx]
        replay_count = 0
        for e in events:
            self.bus.dispatch_locally(e)
            replay_count += 1
        return replay_count
