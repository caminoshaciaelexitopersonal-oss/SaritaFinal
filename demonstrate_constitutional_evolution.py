from sarita_runtime.kernel.civilizational_emergence.constitutional_evolution_engine import EvolutionaryConstitutionalEngine

def run_demo():
    engine = EvolutionaryConstitutionalEngine()
    print(f"Active Constitution: {engine.active_constitution['id']}")

    print("Applying constitutional reform...")
    res = engine.apply_reform("MANDATORY_RECURSIVE_VALIDATION")

    print(f"Reform Status: {res['status']}, Reform ID: {res['reform']['id']}")
    audit = engine.audit_constitutional_evolution()
    print(f"Constitutional Audit: {audit}")

if __name__ == "__main__":
    run_demo()
