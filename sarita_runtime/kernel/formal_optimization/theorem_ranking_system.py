class TheoremRankingSystem:
    """
    Ranks theorems based on their logical strength and constitutional utility.
    """
    def rank_theorems(self, theorems):
        # Ranking criteria: Proof length (shorter is better), GCOI (higher is better)
        ranked = []
        for t in theorems:
            # Score = GCOI * (1 / (ProofLength + 1))
            gcoi = t.get("gcoi", 0.5)
            # Ensure proof_length is at least 0 to avoid zero division
            length = max(0, t.get("proof_length", 10))
            score = gcoi / (length + 1)
            ranked.append({**t, "competition_score": score})

        return sorted(ranked, key=lambda x: x["competition_score"], reverse=True)
