import sys
import os

# Add paths for imports
sys.path.append(os.getcwd())

from sarita_runtime.kernel.sovereign_certification.architectural_novelty_engine import ArchitecturalNoveltyEngine
from sarita_runtime.kernel.sovereign_certification.structural_uniqueness_validator import StructuralUniquenessValidator
from sarita_runtime.kernel.sovereign_certification.evolutionary_innovation_detector import EvolutionaryInnovationDetector
from sarita_runtime.kernel.sovereign_certification.capability_originality_calculator import CapabilityOriginalityCalculator
from sarita_runtime.kernel.sovereign_certification.certification_ledgers import GlobalCertificationLedger

def demonstrate_architectural_novelty():
    print("--- DEMONSTRATING ARCHITECTURAL NOVELTY ---")
    ledger = GlobalCertificationLedger()
    engine = ArchitecturalNoveltyEngine(
        StructuralUniquenessValidator(),
        EvolutionaryInnovationDetector(),
        CapabilityOriginalityCalculator(),
        ledger
    )

    # Evaluate 1M architectures
    report = engine.verify_architectural_novelty([], count=1000000)
    print(f"  Verification Complete: {report['architectures_verified']} architectures analyzed.")
    print(f"  Originality Score: {report['mean_originality_score']}")
    print(f"  Copy Rate: {report['functional_copy_rate']}")

if __name__ == "__main__":
    demonstrate_architectural_novelty()
