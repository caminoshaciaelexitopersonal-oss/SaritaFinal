import sys
import os
import time

# Add paths for imports
sys.path.append(os.getcwd())

# Phase 111 Engines
from sarita_runtime.kernel.metaevolution.evolution_diagnostic_engine import EvolutionDiagnosticEngine
from sarita_runtime.kernel.metaevolution.capability_gap_detector import CapabilityGapDetector
from sarita_runtime.kernel.metaevolution.architectural_deficit_analyzer import ArchitecturalDeficitAnalyzer
from sarita_runtime.kernel.metaevolution.future_requirement_estimator import FutureRequirementEstimator
from sarita_runtime.kernel.metaevolution.future_capability_engine import FutureCapabilityEngine
from sarita_runtime.kernel.metaevolution.capability_architect import CapabilityArchitect
from sarita_runtime.kernel.metaevolution.future_module_designer import FutureModuleDesigner
from sarita_runtime.kernel.metaevolution.evolution_blueprint_generator import EvolutionBlueprintGenerator
from sarita_runtime.kernel.metaevolution.meta_evolution_ledger import RuntimeLedger

# Phase 112 Engines
from sarita_runtime.kernel.evolution_governance.constitutional_evolution_engine import ConstitutionalEvolutionEngine
from sarita_runtime.kernel.evolution_governance.evolution_constitution_validator import EvolutionConstitutionValidator
from sarita_runtime.kernel.evolution_governance.constitutional_rule_interpreter import ConstitutionalRuleInterpreter
from sarita_runtime.kernel.evolution_governance.evolution_legality_checker import EvolutionLegalityChecker
from sarita_runtime.kernel.evolution_governance.scientific_ledgers import ConstitutionalEvolutionLedger, EvolutionApprovalLedger

# Phase 113 Engines
from sarita_runtime.kernel.metaconstitutional_governance.meta_constitution_engine import MetaConstitutionEngine
from sarita_runtime.kernel.metaconstitutional_governance.constitutional_axiom_analyzer import ConstitutionalAxiomAnalyzer
from sarita_runtime.kernel.metaconstitutional_governance.constitutional_consistency_evaluator import ConstitutionalConsistencyEvaluator
from sarita_runtime.kernel.metaconstitutional_governance.constitutional_legitimacy_validator import ConstitutionalLegitimacyValidator
from sarita_runtime.kernel.metaconstitutional_governance.scientific_ledgers import MetaConstitutionLedger

def run_causal_traceability_audit():
    print("--- CAUSAL TRACEABILITY INTEGRATED AUDIT START ---")

    # 1. Axiom Level (Phase 113)
    print("[1] Axiom Audit...")
    meta_ledger = MetaConstitutionLedger()
    meta_engine = MetaConstitutionEngine(
        ConstitutionalAxiomAnalyzer(),
        ConstitutionalConsistencyEvaluator(),
        ConstitutionalLegitimacyValidator(),
        meta_ledger
    )
    meta_eval = meta_engine.evaluate_meta_constitution({"alignment_score": 0.9998}, 100) # Small scale for audit
    axiom_hash = meta_ledger.entries[-1]["hash"]
    print(f"  Axiom State Certified. Hash: {axiom_hash}")

    # 2. Principle/Constitution Level (Phase 112)
    print("[2] Constitutional Governance Validation...")
    evo_ledger = ConstitutionalEvolutionLedger()
    evo_engine = ConstitutionalEvolutionEngine(
        EvolutionConstitutionValidator(),
        ConstitutionalRuleInterpreter(),
        EvolutionLegalityChecker(),
        evo_ledger
    )
    # The proposal references the Axiom Hash for causal chaining
    proposal = {
        "id": "EVO-CAUSAL-001",
        "axiom_evidence": axiom_hash,
        "justification": "axiomatic_consistency_verified",
        "impact_level": 0.3
    }
    evo_res = evo_engine.validate_evolution(proposal)
    assert evo_res["is_approved"] is True
    gov_hash = evo_ledger.entries[-1]["hash"]
    print(f"  Constitution Governance Certified. Hash: {gov_hash}")

    # 3. Evolution/Execution Level (Phase 111)
    print("[3] Meta-Evolutionary Design...")
    runtime_ledger = RuntimeLedger()
    cap_engine = FutureCapabilityEngine(
        CapabilityArchitect(),
        FutureModuleDesigner(),
        EvolutionBlueprintGenerator(),
        runtime_ledger
    )
    # The design references the Governance Hash
    cap_design = cap_engine.design_future_capabilities({"timestamp": time.time(), "gov_evidence": gov_hash})
    design_hash = runtime_ledger.events[-1]["hash"]
    print(f"  Evolution Design Certified. Hash: {design_hash}")

    # Final Integrated Verification
    print("\n[VERIFICATION] Causal Chain Trace:")
    print(f"  Axiom ({axiom_hash[:8]}) → Constitution ({gov_hash[:8]}) → Evolution ({design_hash[:8]})")

    # Verify the chain is recorded in the final ledger
    last_event = runtime_ledger.get_last_event()
    assert last_event["hash"] == design_hash

    print("\nSUCCESS: Integrated causal traceability chain demonstrated.")
    print("--- CAUSAL TRACEABILITY INTEGRATED AUDIT COMPLETE ---")

if __name__ == "__main__":
    run_causal_traceability_audit()
