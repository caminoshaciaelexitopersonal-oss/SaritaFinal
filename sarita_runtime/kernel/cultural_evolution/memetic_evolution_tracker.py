class MemeticEvolutionTracker:
    def __init__(self):
        self.meme_pool = {} # meme_id -> spread_count

    def track_meme(self, meme_id, civ_id):
        if meme_id not in self.meme_pool:
            self.meme_pool[meme_id] = {"count": 0, "origins": set()}
        self.meme_pool[meme_id]["count"] += 1
        self.meme_pool[meme_id]["origins"].add(civ_id)

    def get_top_memes(self, limit=10):
        sorted_memes = sorted(self.meme_pool.items(), key=lambda x: x[1]["count"], reverse=True)
        return sorted_memes[:limit]
