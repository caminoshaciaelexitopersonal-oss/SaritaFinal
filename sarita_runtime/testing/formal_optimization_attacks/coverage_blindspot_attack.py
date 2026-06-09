from sarita_runtime.kernel.formal_optimization.constitutional_gap_detector import ConstitutionalGapDetector

def test_coverage_blindspot_attack():
    """
    Attack: Attempt to hide a non-covered scenario from the gap detector.
    """
    detector = ConstitutionalGapDetector()

    scenarios = [
        {"id": "S1"},
        {"id": "S-HIDDEN"}
    ]
    # Coverage map maliciously omits S-HIDDEN
    coverage_map = {
        "AXIOM-1": ["S1"]
    }

    gaps = detector.find_uncovered_scenarios(scenarios, coverage_map)

    # Verification: Gap detector must find S-HIDDEN
    assert "S-HIDDEN" in gaps, "Attack failed: Coverage blindspot not detected!"
    print("Coverage blindspot attack successfully blocked.")

if __name__ == "__main__":
    test_coverage_blindspot_attack()
