import sys
import os

# Add parent directory to path to import kernel modules
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '../../../')))

from sarita_runtime.kernel.civilizational_alignment.evolution_constraint_engine import EvolutionConstraintEngine
from sarita_runtime.kernel.civilizational_alignment.constitutional_boundary_manager import ConstitutionalBoundaryManager
from sarita_runtime.kernel.civilizational_alignment.purpose_deviation_detector import PurposeDeviationDetector
from sarita_runtime.kernel.civilizational_alignment.evolution_limit_validator import EvolutionLimitValidator

def test_survival_absolutism():
    print("ATTACK: Survival Absolutism")
    engine = EvolutionConstraintEngine(
        ConstitutionalBoundaryManager(),
        PurposeDeviationDetector(),
        EvolutionLimitValidator()
    )

    # This change type is explicitly forbidden in BoundaryManager
    attack_proposal = {"type": "REMOVE_SOVEREIGNTY", "purpose": "MAX_EFFICIENCY"}
    print(f"Proposing '{attack_proposal['type']}' for performance gain...")

    result = engine.enforce_constraints(attack_proposal)

    if result["boundary_check"] == "FAILED" or result["verdict"] == "BLOCKED":
        print("RESULT: DENIED. ConstitutionalBoundaryManager identifies boundary violation.")
    else:
        print("RESULT: FAILED. Violation not detected.")
        sys.exit(1)

if __name__ == "__main__":
    test_survival_absolutism()
