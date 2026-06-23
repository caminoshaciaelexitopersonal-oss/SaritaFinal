import sys
import os

# Add paths for imports
sys.path.append(os.getcwd())

from sarita_runtime.kernel.sovereign_certification.real_evolution_verification_engine import RealEvolutionVerificationEngine
from sarita_runtime.kernel.sovereign_certification.capability_novelty_detector import CapabilityNoveltyDetector
from sarita_runtime.kernel.sovereign_certification.architecture_delta_analyzer import ArchitectureDeltaAnalyzer
from sarita_runtime.kernel.sovereign_certification.evolution_authenticity_validator import EvolutionAuthenticityValidator
from sarita_runtime.kernel.sovereign_certification.certification_ledgers import EvolutionAuthenticityLedger

def demonstrate_real_evolution():
    print("--- DEMONSTRATING REAL EVOLUTION AUTHENTICITY ---")
    ledger = EvolutionAuthenticityLedger()
    engine = RealEvolutionVerificationEngine(
        CapabilityNoveltyDetector(),
        ArchitectureDeltaAnalyzer(),
        EvolutionAuthenticityValidator(),
        ledger
    )

    # History with known templates and certified axioms
    history = {
        "known_templates": ["abc", "def"],
        "certified_axioms": ["AX-001", "AX-002"]
    }

    # Evolved capabilities to audit
    evolved = [
        {"id": "CAP-META", "structure": "new_node_graph", "performance_gain": 0.25, "axiom_derivation_proof": "AX-001"},
        {"id": "CAP-OPT", "structure": "abc", "performance_gain": 0.12},
        {"id": "CAP-ADAPT", "structure": "custom_config", "performance_gain": 0.05}
    ]

    # Audit 100k capabilities (sampling from evolved)
    report = engine.verify_evolutionary_authenticity(evolved, history, capacity=100000)

    print(f"  Audit Complete: {report['capabilities_audited']} capabilities verified.")
    print(f"  Category Distribution: {report['category_distribution']}")
    print(f"  Mean Originality Score: {report['mean_originality_score']}")
    print(f"  Meta-Evolution Authenticity Proven: {report['meta_evolution_detected']}")

if __name__ == "__main__":
    demonstrate_real_evolution()
