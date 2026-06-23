import time

class QuantifiedUncertaintyEngine:
    """
    Engine to assign verifiable uncertainty to every decision.
    """
    def __init__(self, boundary_calc, propagation_engine, probabilistic_certifier, ledger):
        self.boundary_calc = boundary_calc
        self.propagation_engine = propagation_engine
        self.probabilistic_certifier = probabilistic_certifier
        self.ledger = ledger

    def quantify_decision_uncertainty(self, decision_id, evidence_chain):
        print(f"[QuantifiedUncertaintyEngine] Quantifying uncertainty for: {decision_id}...")

        boundaries = self.boundary_calc.calculate_confidence_boundaries(evidence_chain)
        propagated = self.propagation_engine.propagate_uncertainty(boundaries)
        certification = self.probabilistic_certifier.certify_probability(propagated)

        result = {
            "decision_id": decision_id,
            "uncertainty_sigma": round(propagated["sigma"], 4),
            "confidence_interval": [round(c, 4) for c in propagated["interval"]],
            "probabilistic_status": certification["status"],
            "timestamp": time.time()
        }

        self.ledger.record_event("UNCERTAINTY_QUANTIFICATION", result)
        return result
