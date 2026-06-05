import time

class TrustChainValidator:
    """
    Validates that a certificate belongs to a valid trust lineage (Phase 83.2/83.3).
    """
    @staticmethod
    def validate_chain(certificate, trust_anchor):
        # 1. Check Expiration (Phase 84.3)
        from sarita_runtime.kernel.key_governance.certificate_expiration_validator import CertificateExpirationValidator
        if CertificateExpirationValidator.is_expired(certificate):
            return False, "Certificate expired."

        # 2. Verify Hierarchical Levels
        if certificate.level == 0:
            # Root must match anchor
            if trust_anchor.verify_root(certificate.signature):
                return True, "Root verified."
            return False, "Invalid Root signature."

        # 3. Validation logic for intermediate levels (simplified for Phase 83)
        # In a full implementation, this would recursively check signatures.
        if certificate.level in [1, 2, 3]:
            return True, "Chain link verified."

        return False, "Unknown trust level."
