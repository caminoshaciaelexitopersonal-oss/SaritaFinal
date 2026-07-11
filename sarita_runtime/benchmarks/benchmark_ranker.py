class BenchmarkRanker:
    """
    Ranks system configurations based on their normalized benchmark yields.
    """
    def __init__(self):
        pass

    def rank_configurations(self, candidates_scores: dict) -> list:
        # candidates_scores represents a map of name -> score
        ranked = sorted(candidates_scores.items(), key=lambda x: x[1], reverse=True)
        return [{"rank": idx+1, "candidate": name, "score": score} for idx, (name, score) in enumerate(ranked)]
