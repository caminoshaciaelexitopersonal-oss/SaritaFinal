import time

class ConstitutionalKnowledgeBase:
    """
    Stores learned governance knowledge and proven constitutional principles.
    """
    def __init__(self):
        self.patterns = []

    def store_pattern(self, pattern):
        pattern["learned_at"] = time.time()
        self.patterns.append(pattern)

    def get_relevant_patterns(self, context: dict):
        # Return patterns that match the current system context
        return [p for p in self.patterns if p["type"] in context.get("interests", [])]
