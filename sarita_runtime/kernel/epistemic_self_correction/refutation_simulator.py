import time

class RefutationSimulator:
    def simulate_refutation_attempts(self, claim, count=1500000):
        start = time.time()
        counter = 0
        while counter < count:
            counter += 1
        return time.time() - start
