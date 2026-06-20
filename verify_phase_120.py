import time
from sarita_runtime.kernel.scientific_autonomy.recursive_coherence_engine import RecursiveCoherenceEngine
from sarita_runtime.kernel.scientific_autonomy.recursive_convergence_engine import RecursiveConvergenceEngine
from sarita_runtime.kernel.scientific_autonomy.meta_index_governance_engine import MetaIndexGovernanceEngine
from sarita_runtime.kernel.scientific_autonomy.scientific_discovery_engine import ScientificDiscoveryEngine
from sarita_runtime.kernel.scientific_autonomy.theory_competition_engine import TheoryCompetitionEngine
from sarita_runtime.kernel.scientific_autonomy.scientific_autonomy_engine import ScientificAutonomyEngine
from sarita_runtime.kernel.scientific_autonomy.global_scientific_sovereignty_index import GlobalScientificSovereigntyIndex

def verify():
    print("--- Phase 120: Scientific Autonomy & Recursive Coherence Verification ---")

    engines = {
        "coherence": RecursiveCoherenceEngine(),
        "convergence": RecursiveConvergenceEngine(),
        "meta_index": MetaIndexGovernanceEngine(),
        "discovery": ScientificDiscoveryEngine(),
        "theory_comp": TheoryCompetitionEngine(),
        "autonomy": ScientificAutonomyEngine()
    }

    # 1. Recursive Coherence
    print("[1] Verifying Recursive Coherence...")
    state = {"states": [], "components": [], "audit_history": [0.9, 0.95, 0.98]}
    audit = engines["coherence"].audit_coherence(state)
    print(f"    Coherence Score: {audit['coherence_score']:.2f}, Stability: {audit['stability_score']:.4f}")

    # 2. Convergence Certifier
    print("[2] Verifying Convergence Certification...")
    trajectory = [0.8, 0.9, 0.95, 0.95]
    conv = engines["convergence"].evaluate_convergence(trajectory)
    print(f"    Converged: {conv['converged']}, Certified: {conv['certified']}")

    # 3. Scientific Discovery
    print("[3] Verifying Autonomous Discovery Cycle...")
    discovery = engines["discovery"].perform_discovery({"domain_id": "RECURSION"})
    print(f"    Theory Generated: {discovery['theory']['id']}, Refined Score: {discovery['theory']['evidence_score']}")

    # 4. Theory Competition
    print("[4] Verifying Theory Competition...")
    theories = [discovery["theory"], {"id": "T-ALT", "evidence_score": 0.7}]
    comp = engines["theory_comp"].run_competition(theories, [])
    print(f"    Winners: {comp['survivors']}")

    # 5. GSSI Calculation
    print("[5] Calculating GSSI...")
    gssi_engine = GlobalScientificSovereigntyIndex(engines)
    gssi = gssi_engine.get_current_gssi()
    print(f"    Global Scientific Sovereignty Index (GSSI): {gssi:.4f}")

    assert gssi > 0.95, f"GSSI {gssi} below acceptable threshold"
    print("\n✓ Phase 120 Verified Successfully. Cycle 111-120 Sealed.")

if __name__ == "__main__":
    verify()
