import time

class ConstitutionalEvolutionEngine:
    """
    Engine to determine if an evolution is legal, coherent, and constitutional.
    """
    def __init__(self, validator, interpreter, legality_checker, ledger):
        self.validator = validator
        self.interpreter = interpreter
        self.legality_checker = legality_checker
        self.ledger = ledger

    def validate_evolution(self, proposal):
        print(f"[ConstitutionalEvolutionEngine] Validating evolution proposal: {proposal.get('id')}")

        is_legal = self.legality_checker.check_legality(proposal)
        is_coherent = self.validator.verify_coherence(proposal)
        constitutionality = self.interpreter.interpret_constitutional_impact(proposal)

        is_approved = is_legal and is_coherent and constitutionality["score"] > 0.9

        result = {
            "proposal_id": proposal.get("id"),
            "is_legal": is_legal,
            "is_coherent": is_coherent,
            "constitutionality_score": constitutionality["score"],
            "is_approved": is_approved,
            "timestamp": time.time()
        }

        self.ledger.record(result)
        return result
