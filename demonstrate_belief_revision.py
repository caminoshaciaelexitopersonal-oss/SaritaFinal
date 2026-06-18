from sarita_runtime.kernel.epistemic_self_correction.belief_revision_engine import BeliefRevisionEngine

def run_demo():
    engine = BeliefRevisionEngine()
    beliefs = [{"id": "B-001", "entity": "SOVEREIGNTY", "value": "ABSOLUTE", "evidence_strength": 0.5}]
    engine.load_beliefs(beliefs)

    print("Initial Belief:", beliefs[0])

    new_evidence = {"supports": False, "strength": 0.9, "new_value": "METACONSITUTIONAL"}
    revised = engine.process_new_evidence("B-001", new_evidence)

    if revised:
        print("Revised Belief:", revised)
        print("Ledger Hash:", engine.ledger.get_latest_hash())

    # Mass revision demo
    print("Running mass revision simulation (1M beliefs)...")
    stats = engine.run_mass_revision(1000000)
    print(f"Processed: {stats['processed']}, Throughput: {stats['throughput']:.2f} beliefs/sec")

if __name__ == "__main__":
    run_demo()
