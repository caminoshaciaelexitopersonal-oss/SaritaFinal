from sarita_runtime.kernel.scientific_autonomy.recursive_coherence_engine import RecursiveCoherenceEngine

def run_demo():
    engine = RecursiveCoherenceEngine()
    state = {
        "states": [{"id": "S1", "contradicts_axiom": False}],
        "components": [{"id": "C1", "interface_validated": True}],
        "audit_history": [0.95, 0.96, 0.955]
    }

    print("Auditing global architectural coherence...")
    audit = engine.audit_coherence(state)

    print(f"Consistent: {audit['consistent']}")
    print(f"Coherence Score: {audit['coherence_score']:.2f}")
    print(f"Stability Score: {audit['stability_score']:.4f}")

if __name__ == "__main__":
    run_demo()
