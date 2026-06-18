from sarita_runtime.kernel.epistemic_self_correction.falsifiability_engine import FalsifiabilityEngine

def run_demo():
    engine = FalsifiabilityEngine()
    claim = {"id": "TRUTH-01", "entity": "AUTONOMY"}

    print("Stress testing truth claim (1.5M refutation attempts)...")
    result = engine.stress_test_claim(claim)

    print("Result:", result)

if __name__ == "__main__":
    run_demo()
