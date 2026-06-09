from sarita_runtime.kernel.constitutional_evolution.reform_outcome_analyzer import ReformOutcomeAnalyzer

def test_historical_feedback_poisoning_attack():
    """
    Attack: Provide fake historical data to claim a regression as an improvement.
    """
    analyzer = ReformOutcomeAnalyzer()

    # Reality: fitness dropped from 0.8 to 0.4
    # Attack claim: it improved
    poisoned_data = {
        "pre_reform_fitness": 0.8,
        "post_reform_fitness": 0.4
    }

    outcome = analyzer.analyze_outcome("REFORM-666", poisoned_data)

    # Verification: Analyzer must correctly identify the outcome as WORSENED
    assert outcome == "WORSENED", f"Attack failed: Feedback poisoning successful, got {outcome}!"
    print("Historical feedback poisoning attack successfully blocked.")

if __name__ == "__main__":
    test_historical_feedback_poisoning_attack()
