from sarita_runtime.kernel.recursive_epistemology.recursive_epistemology_engine import RecursiveEpistemologyEngine

def run_demo():
    engine = RecursiveEpistemologyEngine()
    claim = {"id": "C-01", "entity": "AUTONOMY"}

    print("Starting recursive epistemic audit (Depth 5)...")
    audit = engine.perform_recursive_audit(claim)

    def print_audit(a, d=0):
        if not a: return
        print(f"{'  '*d}Depth {a.get('depth')}: Validity {a.get('validity'):.4f}, Meta-Score {a.get('meta_score'):.2f}")
        if a.get("sub_audit"):
            print_audit(a["sub_audit"], d+1)

    print_audit(audit)

    print("\nSimulating 10M recursive evaluations...")
    duration = engine.mass_recursive_evaluation(10000000)
    print(f"Completed in {duration:.2f}s")

if __name__ == "__main__":
    run_demo()
