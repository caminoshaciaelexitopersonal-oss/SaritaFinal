class PrescriptionVerifier:
    """
    Verifies that a prescription has cause, evidence, and justification.
    """
    def verify_prescription(self, prescription):
        """
        Ensures the prescription contains all mandatory scientific fields.
        """
        mandatory_fields = ["cause", "evidence", "justification", "expected_outcome"]
        for field in mandatory_fields:
            if not prescription.get(field):
                return False, f"Missing field: {field}"
        return True, "Prescription verified"
