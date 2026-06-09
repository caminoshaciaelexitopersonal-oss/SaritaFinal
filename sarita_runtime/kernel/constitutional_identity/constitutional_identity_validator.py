class ConstitutionalIdentityValidator:
    """
    Validates if a proposed change violates SARITA's core identity.
    """
    def validate_identity_integrity(self, proposal: dict, invariants: list):
        # A proposal violates identity if it modifies or bypasses an invariant principle.
        affected = proposal.get("affected_principles", [])
        for p in affected:
            if p in invariants:
                return False, f"Identity Violation: Modification of Invariant Principle {p}"
        return True, "Identity Integrity Verified."
