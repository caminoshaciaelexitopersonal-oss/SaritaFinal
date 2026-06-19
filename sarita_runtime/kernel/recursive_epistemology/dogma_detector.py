class DogmaDetector:
    def detect_dogma(self, belief, modification_history):
        # A belief is dogmatic if it hasn't changed despite significant negative evidence
        if len(modification_history) == 0 and belief.get("age", 0) > 1000:
            return True
        return False
