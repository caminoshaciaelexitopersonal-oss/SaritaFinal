import sys
import os

# Add paths for imports
sys.path.append(os.getcwd())

from sarita_runtime.kernel.sovereign_certification.scientific_reproducibility_engine import ScientificReproducibilityEngine
from sarita_runtime.kernel.sovereign_certification.causal_reconstruction_engine import CausalReconstructionEngine
from sarita_runtime.kernel.sovereign_certification.ledger_replay_validator import LedgerReplayValidator
from sarita_runtime.kernel.sovereign_certification.evidence_consistency_checker import EvidenceConsistencyChecker
from sarita_runtime.kernel.sovereign_certification.certification_ledgers import ReproducibilityLedger

def demonstrate_scientific_reproducibility():
    print("--- DEMONSTRATING SCIENTIFIC REPRODUCIBILITY ---")
    ledger = ReproducibilityLedger()
    engine = ScientificReproducibilityEngine(
        CausalReconstructionEngine(),
        LedgerReplayValidator(),
        EvidenceConsistencyChecker(),
        ledger
    )

    # Certify 100% reconstruction
    report = engine.certify_reproducibility("HEAD-HASH-X")
    print(f"  Reconstruction Fidelity: {report['reconstruction_fidelity']*100}%")
    print(f"  Evidence Consistency: {report['evidence_consistency']}")
    print(f"  Status: {'CERTIFIED' if report['is_certified'] else 'FAILED'}")

if __name__ == "__main__":
    demonstrate_scientific_reproducibility()
