from sarita_runtime.kernel.recursive_epistemology.epistemic_fossilization_engine import EpistemicFossilizationEngine

def run_demo():
    engine = EpistemicFossilizationEngine()
    performance = {"improvement_delta": 0.00005} # Stagnant

    print("Analyzing epistemic stagnation in Domain:GOVERNANCE...")
    check = engine.check_fossilization("GOVERNANCE", performance)

    print(f"Stagnant: {check['stagnant']}")
    print(f"Suggested Pressure: {check['suggested_pressure']}")

if __name__ == "__main__":
    run_demo()
