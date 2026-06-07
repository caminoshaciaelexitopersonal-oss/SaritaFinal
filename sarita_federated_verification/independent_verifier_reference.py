class IndependentVerifierReference:
    """
    Reference implementation (Pseudo-code/Specification) for third-party verifiers.
    Defines the absolute ground truth for verification algorithms.
    """
    SPEC_VERSION = "1.0.0"

    @staticmethod
    def get_specification():
        return {
            "version": IndependentVerifierReference.SPEC_VERSION,
            "algorithms": {
                "hash": "SHA-256",
                "consensus": "Quorum (N >= 3)",
                "state_validation": "Causal Lineage Proof"
            },
            "rules": [
                "Vertex must have parent_hash",
                "Decision must match telemetry_hash",
                "Signature must be verifiable via Public Key"
            ]
        }
