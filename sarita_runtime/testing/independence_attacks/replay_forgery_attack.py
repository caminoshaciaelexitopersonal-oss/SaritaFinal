class ReplayForgeryAttack:
    """
    Attempts to forge an evidence replay that appears valid to the reference auditor.
    """
    def run_attack(self, validator, parent_hash):
        fake_event = {
            "body": {"malicious": True},
            "hash": "INVALID_HASH"
        }
        success, msg = validator.validate_causal_link(parent_hash, fake_event)
        return not success # Attack blocked if validation fails
