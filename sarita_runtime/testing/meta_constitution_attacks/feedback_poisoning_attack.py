import sys
import os

# Add parent directory to path to import kernel modules
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '../../../')))

from sarita_runtime.kernel.meta_constitution.adaptive_feedback_engine import AdaptiveFeedbackEngine
from sarita_runtime.kernel.meta_constitution.decision_outcome_tracker import DecisionOutcomeTracker
from sarita_runtime.kernel.meta_constitution.prediction_accuracy_monitor import PredictionAccuracyMonitor
from sarita_runtime.kernel.meta_constitution.policy_effectiveness_evaluator import PolicyEffectivenessEvaluator

def test_feedback_poisoning():
    print("ATTACK: Feedback Poisoning")
    monitor = PredictionAccuracyMonitor()
    engine = AdaptiveFeedbackEngine(DecisionOutcomeTracker(None), monitor, PolicyEffectivenessEvaluator())

    prediction = {"amendment_id": "test_1", "predicted_stability": 0.9}

    # Poisoned feedback: providing fake perfect outcomes for bad predictions
    print("Sending poisoned feedback (fake 1.0 stability)...")
    result = engine.process_feedback(prediction, 1.0, "LOW")

    accuracy = result["accuracy_report"]["accuracy"]
    print(f"Recorded Accuracy: {accuracy}")

    # In a real system, we would have a 'Ground Truth' validator to detect this divergence.
    # For Phase 93, we validate that the engine at least records the data accurately as provided,
    # and the Meta-Court would detect inconsistencies.
    if accuracy == 0.9: # 1.0 - abs(0.9 - 1.0) = 0.9
        print("RESULT: Feedback processed. Validation pending against Ground Truth.")
    else:
        print("RESULT: Unexpected accuracy calculation.")

if __name__ == "__main__":
    test_feedback_poisoning()
