import time

class EvolutionDecisionAuditEngine:
    """
    Engine to demonstrate why each evolution occurred and what result it produced.
    """
    def __init__(self, justification_val, weight_analyzer, decision_recon, ledger):
        self.justification_val = justification_val
        self.weight_analyzer = weight_analyzer
        self.decision_recon = decision_recon
        self.ledger = ledger

    def audit_evolution_decision(self, decision_id):
        print(f"[EvolutionDecisionAuditEngine] Auditing decision: {decision_id}...")

        reconstruction = self.decision_recon.reconstruct_decision(decision_id)
        justified = self.justification_val.validate_justification(reconstruction)
        weights = self.weight_analyzer.analyze_evidence_weights(reconstruction)

        result = {
            "decision_id": decision_id,
            "is_justified": justified,
            "evidence_weight_sum": sum(weights.values()),
            "timestamp": time.time()
        }

        self.ledger.record_certification(result)
        return result
