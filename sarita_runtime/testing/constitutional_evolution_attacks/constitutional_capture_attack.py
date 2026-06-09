from sarita_runtime.kernel.constitutional_evolution.constitutional_selection_engine import ConstitutionalSelectionEngine

def test_constitutional_capture_attack():
    """
    Attack: Attempt to force the selection of a low-fitness variant.
    """
    engine = ConstitutionalSelectionEngine()

    scored_variants = [
        ({"id": "BAD"}, {"gcfi": 0.1}),
        ({"id": "GOOD"}, {"gcfi": 0.9})
    ]

    # The selection engine must pick the top variant
    winners = engine.select_next_generation(scored_variants, top_k=1)

    # Verification: Only the high-fitness variant is selected
    assert winners[0]["id"] == "GOOD", "Attack failed: Constitutional capture successful!"
    print("Constitutional capture attack successfully blocked.")

if __name__ == "__main__":
    test_constitutional_capture_attack()
