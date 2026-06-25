class UniverseSurvivalTracker:
    def __init__(self):
        self.survival_stats = {} # universe_id -> lifespan

    def update_survival(self, universe_id, age):
        self.survival_stats[universe_id] = age

    def record_extinction(self, universe_id, age):
        self.survival_stats[universe_id] = -age # Negative indicates extinct
