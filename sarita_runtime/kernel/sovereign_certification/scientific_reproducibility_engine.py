import time

class ScientificReproducibilityEngine:
    """
    Engine to reconstruct the full evolution chain from ledgers and hashes.
    """
    def __init__(self, causal_recon, replay_val, evidence_checker, ledger):
        self.causal_recon = causal_recon
        self.replay_val = replay_val
        self.evidence_checker = evidence_checker
        self.ledger = ledger

    def certify_reproducibility(self, target_chain_head):
        print(f"[ScientificReproducibilityEngine] Reconstructing causal chain for head: {target_chain_head[:8]}...")

        reconstruction = self.causal_recon.reconstruct_chain(target_chain_head)
        replay_match = self.replay_val.validate_replay(reconstruction)
        consistency = self.evidence_checker.check_consistency(reconstruction)

        result = {
            "reconstruction_fidelity": 1.0 if replay_match else 0.0,
            "evidence_consistency": consistency,
            "is_certified": replay_match and consistency > 0.99,
            "timestamp": time.time()
        }

        self.ledger.record_certification(result)
        return result
