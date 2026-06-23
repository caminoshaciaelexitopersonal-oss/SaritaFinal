from sarita_runtime.kernel.civilizational_emergence.cognitive_government_engine import CognitiveGovernmentEngine

def run_demo():
    engine = CognitiveGovernmentEngine()
    print("Executing sovereign governance cycle...")
    res = engine.perform_governance_cycle("RECURSIVE_INTEGRITY")

    print(f"Separation of Powers: {res['separation_of_powers']}")
    print(f"Governance Fidelity: {res['governance_fidelity']}")
    print(f"Judicial Audit Result: {res['audit']['audit_passed']}")

if __name__ == "__main__":
    run_demo()
