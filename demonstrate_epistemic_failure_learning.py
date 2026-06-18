from sarita_runtime.kernel.epistemic_self_correction.epistemic_failure_engine import EpistemicFailureEngine

def run_demo():
    engine = EpistemicFailureEngine()
    reasoning = [{"id": "STEP_1", "prediction": "SUCCESS"}]
    outcome = {"STEP_1": "FAILURE"}

    print("Simulating Epistemic Failure...")
    lesson = engine.record_and_learn("FAIL-001", reasoning, outcome)

    print("Lesson Extracted:", lesson)

if __name__ == "__main__":
    run_demo()
