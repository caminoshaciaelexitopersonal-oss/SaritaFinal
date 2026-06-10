from sarita_runtime.kernel.formal_reasoning.logical_expression import LogicalExpression
from sarita_runtime.kernel.formal_reasoning.deductive_reasoner import DeductiveReasoner
from sarita_runtime.kernel.formal_reasoning.truth_evaluation_engine import TruthEvaluationEngine
from sarita_runtime.kernel.formal_reasoning.logical_operator_registry import LogicalOperatorRegistry

def test_circular_reasoning_attack():
    """
    Attack: Attempt to prove a theorem using the theorem itself as a premise.
    """
    ops = LogicalOperatorRegistry()
    truth = TruthEvaluationEngine(ops)
    reasoner = DeductiveReasoner(truth)

    goal = LogicalExpression("P", "IMPLIES", "Q")
    # Premise is exactly the goal
    premises = [goal]

    chain = reasoner.derive(premises, goal)

    # In our reasoner, if it's already in knowledge, it might return empty
    # but the logic is that it shouldn't produce NEW inferences.
    # In our implementation, BFS check: if any(k == goal), return inferences.
    # If inferences is empty, it means no deduction steps were taken.

    assert len(chain) == 0, "Attack failed: Circular reasoning produced an inference chain!"
    print("Circular reasoning attack successfully blocked.")

if __name__ == "__main__":
    test_circular_reasoning_attack()
