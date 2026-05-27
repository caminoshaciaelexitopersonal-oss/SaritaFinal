import logging
import threading
from collections import deque

class HighPerformanceQueue:
    """
    High-performance thread-safe queue.
    Uses fine-grained locking on a deque for minimal contention.
    (Note: True lock-free in Python is limited by the GIL;
    this provides the material material performance needed for the physical path).
    """
    def __init__(self, capacity: int = 1000):
        self._queue = deque()
        self._lock = threading.Lock()
        self._capacity = capacity
        self._not_full = threading.Condition(self._lock)
        self._not_empty = threading.Condition(self._lock)

    def put(self, item, block=True):
        with self._lock:
            if block:
                while len(self._queue) >= self._capacity:
                    self._not_full.wait()
            elif len(self._queue) >= self._capacity:
                return False

            self._queue.append(item)
            self._not_empty.notify()
            return True

    def get(self, block=True):
        with self._lock:
            if block:
                while not self._queue:
                    self._not_empty.wait()
            elif not self._queue:
                return None

            item = self._queue.popleft()
            self._not_full.notify()
            return item

    def qsize(self):
        return len(self._queue)
