from sarita_runtime.kernel.scientific_civilization.scientific_constitution_engine import ScientificConstitutionEngine

def run_demo():
    engine = ScientificConstitutionEngine()
    theory = {"id": "T-01", "evidence": 0.85, "contradicts_axiom": False}
    ops = [{"id": "OP-1", "violated_rule": False}]

    print("Enforcing scientific constitution...")
    res = engine.enforce_constitution(theory, ops)

    print(f"Theory Admission Granted: {res['admission_granted']}")
    print(f"Scientific Audit Passed: {res['audit_passed']}")

if __name__ == "__main__":
    run_demo()
