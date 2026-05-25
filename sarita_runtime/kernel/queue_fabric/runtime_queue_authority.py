import logging
import threading
from collections import deque
import itertools

class LockFreeQueue:
    """
    Optimized high-performance queue.
    While true non-blocking lock-free is complex in Python,
    this uses a fine-grained mutex-protected deque which is standard for
    high-concurrency threading.
    """
    def __init__(self, capacity: int = 1000):
        self._queue = deque()
        self._lock = threading.Lock()
        self._capacity = capacity
        self._not_full = threading.Condition(self._lock)
        self._not_empty = threading.Condition(self._lock)
        self._counter = itertools.count()

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
