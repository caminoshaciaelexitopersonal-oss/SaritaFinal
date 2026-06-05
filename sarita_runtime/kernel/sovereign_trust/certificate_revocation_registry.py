import time
import logging

class CertificateRevocationRegistry:
    """
    Registry for invalidated certificates (Phase 83.4).
    """
    def __init__(self):
        self.revoked_ids = set()
        self.quarantined_ids = {}

    def revoke(self, subject_id: str, reason: str):
        logging.critical(f"TRUST REVOCATION: Certificate for '{subject_id}' revoked. Reason: {reason}")
        self.revoked_ids.add(subject_id)

    def quarantine(self, subject_id: str, duration: int = 3600):
        expiry = time.time() + duration
        self.quarantined_ids[subject_id] = expiry
        logging.warning(f"TRUST QUARANTINE: Component '{subject_id}' quarantined until {time.ctime(expiry)}")

    def is_valid(self, subject_id: str):
        if subject_id in self.revoked_ids:
            return False

        if subject_id in self.quarantined_ids:
            if time.time() < self.quarantined_ids[subject_id]:
                return False
            else:
                del self.quarantined_ids[subject_id]
        return True
