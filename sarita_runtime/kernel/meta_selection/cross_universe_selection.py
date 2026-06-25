class CrossUniverseSelection:
    def __init__(self):
        pass

    def perform_selection(self, scored_universes, threshold=0.3):
        # Cull universes with very low relative fitness
        max_score = scored_universes[0][1] if scored_universes else 1.0
        selected = [u for u, score in scored_universes if score > max_score * threshold]
        culled = [u for u, score in scored_universes if score <= max_score * threshold]
        return selected, culled
