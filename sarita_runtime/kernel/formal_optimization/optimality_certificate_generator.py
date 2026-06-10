import time

class OptimalityCertificateGenerator:
    """
    Generates the final optimality certificate for a proven decision.
    """
    def generate(self, proof_id, winner_id):
        return {
            "certificate_id": f"CERT-{proof_id}",
            "winner_id": winner_id,
            "validity": "MATHEMATICALLY_PROVEN_OPTIMUM",
            "timestamp": time.time()
        }
