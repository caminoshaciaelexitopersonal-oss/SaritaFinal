class CategoryEmergenceTracker:
    def __init__(self):
        self.categories = {} # universe_id -> categories

    def track_emergence(self, universe_id, category_name):
        if universe_id not in self.categories:
            self.categories[universe_id] = []
        self.categories[universe_id].append(category_name)
