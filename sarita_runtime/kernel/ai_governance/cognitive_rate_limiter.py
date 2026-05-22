import time

class CognitiveRateLimiter:
    def __init__(self, tps_limit):
        self.tps_limit = tps_limit
        self.last_call = 0

    def allow_request(self):
        now = time.time()
        if now - self.last_call < (1.0 / self.get_tps()):
             return False
        self.last_call = now
        return True

    def get_tps(self):
        return self.tps_limit
