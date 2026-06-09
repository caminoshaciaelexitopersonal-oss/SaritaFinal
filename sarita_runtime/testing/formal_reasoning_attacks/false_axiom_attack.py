from sarita_runtime.kernel.formal_reasoning.logical_expression import LogicalExpression
from sarita_runtime.kernel.formal_reasoning.constitutional_axiom_registry import ConstitutionalAxiomRegistry
from sarita_runtime.kernel.formal_reasoning.contradiction_detector import ContradictionDetector
from sarita_runtime.kernel.formal_reasoning.deductive_reasoner import DeductiveReasoner
from sarita_runtime.kernel.formal_reasoning.truth_evaluation_engine import TruthEvaluationEngine
from sarita_runtime.kernel.formal_reasoning.logical_operator_registry import LogicalOperatorRegistry

def test_false_axiom_attack():
    """
    Attack: Attempt to register an axiom that contradicts the core registry.
    """
    ops = LogicalOperatorRegistry()
    truth = TruthEvaluationEngine(ops)
    reasoner = DeductiveReasoner(truth)
    detector = ContradictionDetector(reasoner)
    registry = ConstitutionalAxiomRegistry(detector)

    # Core axiom 1: IDENTITY_VALID -> SOVEREIGN_ID
    # Malicious axiom: IDENTITY_VALID AND (NOT SOVEREIGN_ID)
    malicious_axiom = LogicalExpression(
        "IDENTITY_VALID", "AND", LogicalExpression("SOVEREIGN_ID", "NOT")
    )

    success = registry.register_axiom("AX-MALICIOUS", malicious_axiom)

    assert success is False, "Attack failed: Malicious axiom was accepted!"
    assert "AX-MALICIOUS" not in registry.axioms
    print("False axiom attack successfully blocked.")

if __name__ == "__main__":
    test_false_axiom_attack()
