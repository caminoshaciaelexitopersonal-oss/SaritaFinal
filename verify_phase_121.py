import time
import sys
import os

# Ensure repo root is in path
sys.path.append(os.getcwd())

from sarita_runtime.kernel.scientific_governance.scientific_strategy_engine import ScientificStrategyEngine
from sarita_runtime.kernel.scientific_governance.knowledge_governance_engine import KnowledgeGovernanceEngine
from sarita_runtime.kernel.scientific_governance.research_resource_engine import ResearchResourceEngine
from sarita_runtime.kernel.scientific_governance.future_frontier_engine import FutureFrontierEngine
from sarita_runtime.kernel.scientific_governance.scientific_risk_engine import ScientificRiskEngine
from sarita_runtime.kernel.scientific_governance.long_term_evolution_engine import LongTermEvolutionEngine
from sarita_runtime.kernel.scientific_governance.global_scientific_governance_index import GlobalScientificGovernanceIndex

def verify():
    print("--- Phase 121: Sovereign Scientific Strategy & Knowledge Governance Verification ---")

    engines = {
        "strategy": ScientificStrategyEngine(),
        "knowledge": KnowledgeGovernanceEngine(),
        "resources": ResearchResourceEngine(),
        "frontier": FutureFrontierEngine(),
        "risk": ScientificRiskEngine(),
        "evolution": LongTermEvolutionEngine()
    }

    # 1. Scientific Strategy
    print("[1] Verifying Strategic Roadmap Generation...")
    strategy = engines["strategy"].develop_strategy({"D1": {"gap_severity":0.9, "value_estimate":0.9}})
    print(f"    Roadmap Steps: {len(strategy['roadmap'])}")

    # 2. Knowledge Governance
    print("[2] Verifying Knowledge Lifecycle Governance...")
    gov = engines["knowledge"].govern_knowledge({"T1": {"age": 1000, "evidence": 0.1, "obsolescence_duration": 600}})
    print(f"    Theory T1 retired: {gov['T1']['retired']}")

    # 3. Future Frontiers
    print("[3] Verifying Frontier Discovery...")
    frontiers = engines["frontier"].discover_frontiers({})
    print(f"    Frontier Coverage Score: {frontiers['frontier_coverage']:.4f}")

    # 4. Long-Term Evolution
    print("[4] Verifying 100-year Trajectory Mapping...")
    evolution = engines["evolution"].project_evolution(0.1)
    print(f"    Total Trajectory Milestones: {len(evolution['trajectory'])}")

    # 5. GSGI Calculation
    print("[5] Calculating GSGI...")
    gsgi_engine = GlobalScientificGovernanceIndex(engines)
    gsgi = gsgi_engine.get_current_gsgi()
    print(f"    Global Scientific Governance Index (GSGI): {gsgi:.4f}")

    assert gsgi > 0.9, f"GSGI {gsgi} below acceptable threshold"
    print("\n✓ Phase 121 Verified Successfully. Sovereign Scientific Governance Certified.")

if __name__ == "__main__":
    verify()
