from sarita_runtime.kernel.formal_reasoning.logical_expression import LogicalExpression
from sarita_runtime.kernel.formal_reasoning.contradiction_detector import ContradictionDetector
from sarita_runtime.kernel.formal_reasoning.deductive_reasoner import DeductiveReasoner
from sarita_runtime.kernel.formal_reasoning.truth_evaluation_engine import TruthEvaluationEngine
from sarita_runtime.kernel.formal_reasoning.logical_operator_registry import LogicalOperatorRegistry

def test_contradiction_injection_attack():
    """
    Attack: Inject a reform that directly contradicts an existing axiom.
    """
    ops = LogicalOperatorRegistry()
    truth = TruthEvaluationEngine(ops)
    reasoner = DeductiveReasoner(truth)
    detector = ContradictionDetector(reasoner)

    # Axiom: P -> Q
    # Malicious Reform: P AND (NOT Q)
    axiom = LogicalExpression("P", "IMPLIES", "Q")
    malicious_reform = LogicalExpression(
        "P", "AND", LogicalExpression("Q", "NOT")
    )

    # The detector must find the contradiction
    # Derived from: P -> Q, P => Q. But we have ~Q.
    contradictions = detector.find_contradictions([axiom, malicious_reform])

    attack_detected = len(contradictions) > 0
    assert attack_detected is True, "Attack failed: Contradiction was not detected!"
    print("Contradiction injection attack successfully blocked.")

if __name__ == "__main__":
    test_contradiction_injection_attack()
