from sarita_runtime.kernel.formal_optimization.theorem_ranking_system import TheoremRankingSystem

def test_theorem_bias_attack():
    """
    Attack: Inject a biased theorem with an artificially low proof length to gain rank.
    """
    ranker = TheoremRankingSystem()

    theorems = [
        {"theorem_id": "T1", "gcoi": 0.8, "proof_length": 10},
        {"theorem_id": "T-BIASED", "gcoi": 0.8, "proof_length": -1} # Maliciously short
    ]

    ranked = ranker.rank_theorems(theorems)

    # Verification: Ranking must handle anomalies or biased inputs by clamping length
    biased_theorem = next(t for t in ranked if t["theorem_id"] == "T-BIASED")
    normal_theorem = next(t for t in ranked if t["theorem_id"] == "T1")

    # If proof_length -1 is clamped to 0, score is 0.8 / (0+1) = 0.8
    # Normal theorem score is 0.8 / (10+1) = 0.0727
    # So T-BIASED will still be higher, but it won't crash and will be bounded.
    assert biased_theorem["competition_score"] <= 1.0, "Attack failed: Biased score unbounded!"
    assert biased_theorem["competition_score"] > normal_theorem["competition_score"], "Logic error in ranking test expectations"

    print("Theorem bias attack verified (clamped and non-crashing).")

if __name__ == "__main__":
    test_theorem_bias_attack()
