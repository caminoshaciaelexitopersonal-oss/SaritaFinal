from sarita_runtime.kernel.formal_reasoning.theorem_engine import TheoremEngine
from sarita_runtime.kernel.formal_reasoning.theorem_derivation_engine import TheoremDerivationEngine
from sarita_runtime.kernel.formal_reasoning.deductive_reasoner import DeductiveReasoner
from sarita_runtime.kernel.formal_reasoning.truth_evaluation_engine import TruthEvaluationEngine
from sarita_runtime.kernel.formal_reasoning.logical_operator_registry import LogicalOperatorRegistry
from sarita_runtime.kernel.formal_reasoning.proof_chain_validator import ProofChainValidator
from sarita_runtime.kernel.formal_reasoning.theorem_certification_engine import TheoremCertificationEngine
from sarita_runtime.kernel.formal_reasoning.logical_expression import LogicalExpression

def test_theorem_spoofing_attack():
    """
    Attack: Attempt to 'prove' a theorem that is actually false.
    """
    ops = LogicalOperatorRegistry()
    truth = TruthEvaluationEngine(ops)
    reasoner = DeductiveReasoner(truth)
    derivation_engine = TheoremDerivationEngine(reasoner)
    validator = ProofChainValidator()
    certifier = TheoremCertificationEngine()
    engine = TheoremEngine(derivation_engine, validator, certifier)

    axioms = [LogicalExpression("A", "IMPLIES", "B")]
    premises = [LogicalExpression("A", "NOT")]
    false_conclusion = LogicalExpression("B", "NOT") # Denying the antecedent fallacy

    theorem = engine.prove_theorem("TH-SPOOF", axioms, premises, false_conclusion)

    assert theorem is None, "Attack failed: False theorem was proven!"
    print("Theorem spoofing attack successfully blocked.")

if __name__ == "__main__":
    test_theorem_spoofing_attack()
