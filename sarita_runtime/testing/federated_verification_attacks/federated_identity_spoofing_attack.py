class FederatedIdentitySpoofingAttack:
    """
    Simulates an attacker pretending to be a registered auditor from a trusted domain.
    """
    def run_attack(self, registry, fake_id):
        auditor = registry.get_auditor(fake_id)
        if auditor is None:
            return True, "Attack blocked: Spoofed identity not found in registry."
        return False, "Attack succeeded: Spoofed identity accepted."
