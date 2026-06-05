import time
import logging

class CertificateExpirationValidator:
    """
    Verifies that certificates are within their validity period (Phase 84.3).
    """
    @staticmethod
    def is_expired(certificate):
        now = time.time()
        if now > certificate.expiry_date:
            logging.error(f"CERTIFICATE EXPIRED: {certificate.subject_id} expired at {time.ctime(certificate.expiry_date)}")
            return True
        return False

    @staticmethod
    def is_not_yet_valid(certificate):
        if hasattr(certificate, 'valid_from') and time.time() < certificate.valid_from:
            return True
        return False
