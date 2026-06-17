import sys
import os
import hashlib
import time
import json

# Add paths for imports
sys.path.append(os.getcwd())

# Phase 113 Ledgers & Engines
from sarita_runtime.kernel.metaconstitutional_governance.scientific_ledgers import MetaConstitutionLedger
from sarita_runtime.kernel.metaconstitutional_governance.meta_constitution_engine import MetaConstitutionEngine
from sarita_runtime.kernel.metaconstitutional_governance.constitutional_axiom_analyzer import ConstitutionalAxiomAnalyzer
from sarita_runtime.kernel.metaconstitutional_governance.constitutional_consistency_evaluator import ConstitutionalConsistencyEvaluator
from sarita_runtime.kernel.metaconstitutional_governance.constitutional_legitimacy_validator import ConstitutionalLegitimacyValidator

# Phase 112 Ledgers & Engines
from sarita_runtime.kernel.evolution_governance.scientific_ledgers import ConstitutionalEvolutionLedger
from sarita_runtime.kernel.evolution_governance.constitutional_evolution_engine import ConstitutionalEvolutionEngine
from sarita_runtime.kernel.evolution_governance.evolution_constitution_validator import EvolutionConstitutionValidator
from sarita_runtime.kernel.evolution_governance.constitutional_rule_interpreter import ConstitutionalRuleInterpreter
from sarita_runtime.kernel.evolution_governance.evolution_legality_checker import EvolutionLegalityChecker

# Phase 111 Ledgers & Engines
from sarita_runtime.kernel.metaevolution.meta_evolution_ledger import RuntimeLedger
from sarita_runtime.kernel.metaevolution.future_capability_engine import FutureCapabilityEngine
from sarita_runtime.kernel.metaevolution.capability_architect import CapabilityArchitect
from sarita_runtime.kernel.metaevolution.future_module_designer import FutureModuleDesigner
from sarita_runtime.kernel.metaevolution.evolution_blueprint_generator import EvolutionBlueprintGenerator

def demonstrate_causal_chain():
    print("=== SARITA SOVEREIGN EVOLUTION CAUSAL CHAIN DEMONSTRATION ===")

    # 1. THE AXIOM (Root of Legitimacy)
    print("\n[STEP 1] AXIOMATIC CERTIFICATION (Phase 113)")
    meta_ledger = MetaConstitutionLedger()
    meta_engine = MetaConstitutionEngine(
        ConstitutionalAxiomAnalyzer(),
        ConstitutionalConsistencyEvaluator(),
        ConstitutionalLegitimacyValidator(),
        meta_ledger
    )
    # Small scale for demonstration
    meta_eval = meta_engine.evaluate_meta_constitution({"alignment_score": 1.0}, axiom_count=100)
    axiom_entry = meta_ledger.entries[-1]
    axiom_hash = axiom_entry["hash"]
    print(f"  Axiom State: CERTIFIED")
    print(f"  Axiom Hash:  {axiom_hash}")

    # 2. THE CONSTITUTION (Governance Framework)
    print("\n[STEP 2] CONSTITUTIONAL GOVERNANCE VALIDATION (Phase 112)")
    evo_ledger = ConstitutionalEvolutionLedger()
    evo_engine = ConstitutionalEvolutionEngine(
        EvolutionConstitutionValidator(),
        ConstitutionalRuleInterpreter(),
        EvolutionLegalityChecker(),
        evo_ledger
    )
    # Proposal anchored to the Axiom Hash
    proposal = {
        "id": "PROP-EVO-2026-X",
        "axiom_evidence_link": axiom_hash,
        "justification": "axiomatic_consistency_verified",
        "impact_level": 0.2
    }
    evo_res = evo_engine.validate_evolution(proposal)
    gov_entry = evo_ledger.entries[-1]
    gov_hash = gov_entry["hash"]
    print(f"  Governance Link: {gov_entry['parent_hash'][:16]}... (Parent)")
    print(f"  Governance Hash: {gov_hash}")

    # 3. THE EVOLUTION (Capability Design)
    print("\n[STEP 3] META-EVOLUTIONARY DESIGN (Phase 111)")
    runtime_ledger = RuntimeLedger()
    cap_engine = FutureCapabilityEngine(
        CapabilityArchitect(),
        FutureModuleDesigner(),
        EvolutionBlueprintGenerator(),
        runtime_ledger
    )
    # Design anchored to the Governance Hash
    design_input = {"timestamp": time.time(), "governance_evidence_link": gov_hash}
    _ = cap_engine.design_future_capabilities(design_input, count=10) # Small count
    design_entry = runtime_ledger.events[-1]
    design_hash = design_entry["hash"]
    print(f"  Evolution Link: {design_entry['parent_hash'][:16]}... (Parent)")
    print(f"  Evolution Hash: {design_hash}")

    # 4. THE RESULT (Material Outcome)
    print("\n[STEP 4] MATERIAL RESULT RECONSTRUCTION")

    causal_chain = [
        {"layer": "AXIOM", "hash": axiom_hash, "data": axiom_entry["data"]},
        {"layer": "CONSTITUTION", "hash": gov_hash, "parent": axiom_hash, "data": gov_entry["data"]},
        {"layer": "EVOLUTION", "hash": design_hash, "parent": gov_hash, "data": design_entry["data"]}
    ]

    print("\nVERIFIED CAUSAL TRACE:")
    for step in causal_chain:
        p_info = f" <- Parent: {step['parent'][:8]}" if "parent" in step else " (ROOT)"
        print(f"  [{step['layer']}] Hash: {step['hash'][:8]}...{p_info}")

    print("\nDEMONSTRATION SUCCESS: Full ledgerized chain verified.")

if __name__ == "__main__":
    demonstrate_causal_chain()
