import collections

class EventStream:
    """
    In-memory streaming pipeline for high-performance event ingestion.
    """
    def __init__(self, capacity: int = 10000):
        self.stream = collections.deque(maxlen=capacity)

    def append(self, event):
        self.stream.append(event)

    def read_all(self) -> list:
        return list(self.stream)

    def clear(self):
        self.stream.clear()
