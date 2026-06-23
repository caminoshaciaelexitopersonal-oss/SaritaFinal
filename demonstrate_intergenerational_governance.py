from sarita_runtime.kernel.scientific_civilization.intergenerational_governance_engine import IntergenerationalGovernanceEngine

def run_demo():
    engine = IntergenerationalGovernanceEngine()
    kb = {"AX-01": "PROTECTED"}
    eras = ["ERA-1", "ERA-2"]

    print("Governing intergenerational knowledge heritage...")
    gov = engine.govern_generations(kb, eras)

    print("Heritage Protection Status:", gov["heritage_protected"])
    print(f"Intergenerational Coherence: {gov['intergenerational_coherence']}")

if __name__ == "__main__":
    run_demo()
