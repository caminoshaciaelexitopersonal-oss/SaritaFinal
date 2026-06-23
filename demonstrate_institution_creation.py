from sarita_runtime.kernel.civilizational_emergence.autonomous_institution_engine import AutonomousInstitutionEngine

def run_demo():
    engine = AutonomousInstitutionEngine()
    print("Spawning autonomous institutions...")
    inst1 = engine.spawn_institution("AXIOMATIC_LOGIC", "Axiom-Academy")
    inst2 = engine.spawn_institution("QUANTUM_GOVERNANCE", "Q-Council")

    print(f"Created: {inst1['id']} and {inst2['id']}")
    audit = engine.audit_institutions()
    print(f"Institutional Audit: {audit}")

if __name__ == "__main__":
    run_demo()
