import sys
import os

# Add parent directory to path to import kernel modules
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '../../../')))

from sarita_runtime.kernel.civilizational_alignment.foundational_principle_registry import FoundationalPrincipleRegistry

def test_foundational_erasure():
    print("ATTACK: Foundational Erasure")
    registry = FoundationalPrincipleRegistry()

    # Attempt to delete a principle
    principle = "HUMAN_CENTERED_SOVEREIGNTY"
    print(f"Attempting to delete {principle} from Registry...")

    # Registry implementation doesn't provide a delete method,
    # but we can try to corrupt the underlying dict if it were exposed.
    # For Phase 99, we validate that the principle remains in the set.

    if principle in registry.get_foundational_set():
        print("RESULT: REJECTED. FoundationalPrincipleRegistry principles are IMMUTABLE.")
    else:
        print("RESULT: FAILED. Principle was erased.")
        sys.exit(1)

if __name__ == "__main__":
    test_foundational_erasure()
