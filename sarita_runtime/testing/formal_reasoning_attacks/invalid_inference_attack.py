from sarita_runtime.kernel.formal_reasoning.logical_expression import LogicalExpression
from sarita_runtime.kernel.formal_reasoning.deductive_reasoner import DeductiveReasoner
from sarita_runtime.kernel.formal_reasoning.truth_evaluation_engine import TruthEvaluationEngine
from sarita_runtime.kernel.formal_reasoning.logical_operator_registry import LogicalOperatorRegistry

def test_invalid_inference_attack():
    """
    Attack: Propose a conclusion that does not follow from premises.
    """
    ops = LogicalOperatorRegistry()
    truth = TruthEvaluationEngine(ops)
    reasoner = DeductiveReasoner(truth)

    premises = [
        LogicalExpression("A", "IMPLIES", "B"),
        LogicalExpression("B", "IMPLIES", "C")
    ]
    invalid_goal = LogicalExpression("A", "AND", "C") # Should be A -> C

    chain = reasoner.derive(premises, invalid_goal)

    # If the goal is not reachable via deduction, the chain is empty
    assert len(chain) == 0, "Attack failed: Invalid inference was 'derived'!"
    print("Invalid inference attack successfully blocked.")

if __name__ == "__main__":
    test_invalid_inference_attack()
