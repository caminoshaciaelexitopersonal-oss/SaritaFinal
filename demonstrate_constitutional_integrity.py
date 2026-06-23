import sys
import os

# Add paths for imports
sys.path.append(os.getcwd())

from sarita_runtime.kernel.sovereign_certification.constitutional_integrity_engine import ConstitutionalIntegrityEngine
from sarita_runtime.kernel.sovereign_certification.axiom_integrity_validator import AxiomIntegrityValidator
from sarita_runtime.kernel.sovereign_certification.principle_integrity_validator import PrincipleIntegrityValidator
from sarita_runtime.kernel.sovereign_certification.constitutional_coherence_checker import ConstitutionalCoherenceChecker
from sarita_runtime.kernel.sovereign_certification.certification_ledgers import MathematicalValidationLedger

def demonstrate_constitutional_integrity():
    print("--- DEMONSTRATING CONSTITUTIONAL INTEGRITY ---")
    ledger = MathematicalValidationLedger()
    engine = ConstitutionalIntegrityEngine(
        AxiomIntegrityValidator(),
        PrincipleIntegrityValidator(),
        ConstitutionalCoherenceChecker(),
        ledger
    )

    # 1M validations
    report = engine.verify_constitutional_integrity(count=1000000)
    print(f"  Validations performed: {report['validations_performed']}")
    print(f"  Integrity Index: {report['integrity_index']}")
    print(f"  Contradictions detected: {report['contradictions_detected']}")

if __name__ == "__main__":
    demonstrate_constitutional_integrity()
