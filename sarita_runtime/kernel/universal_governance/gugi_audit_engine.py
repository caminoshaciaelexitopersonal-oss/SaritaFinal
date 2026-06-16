class GUGIAuditEngine:
    """
    Engine for auditing and reconstructing the Global Universal Governance Index.
    """
    def __init__(self, validator, rebuilder, ledger):
        self.validator = validator
        self.rebuilder = rebuilder
        self.ledger = ledger

    def audit_gugi(self, certified_gugi, raw_evidence):
        """
        Reconstructs GUGI and verifies it against the certified version.
        """
        # 1. Traceability Check
        is_traceable = self.validator.validate_gugi_components(certified_gugi)

        # 2. Reconstruction
        reconstructed_value = self.rebuilder.rebuild_metric(raw_evidence)

        # 3. Verification
        # In a real system, we compare bit-for-bit or with epsilon
        is_consistent = abs(reconstructed_value - certified_gugi["value"]) < 0.0001

        # Mandatory check: reconstructed_gugi == certified_gugi
        assert is_consistent, f"GUGI Reconstruction failed: {reconstructed_value} != {certified_gugi['value']}"

        report = {
            "certified_gugi": certified_gugi["value"],
            "reconstructed_gugi": reconstructed_value,
            "is_traceable": is_traceable,
            "is_consistent": is_consistent,
            "status": "CERTIFIED" if is_consistent and is_traceable else "REJECTED"
        }

        if self.ledger:
            self.ledger.record_gugi_audit(report)

        self._generate_report_file(report)
        return report

    def _generate_report_file(self, report):
        with open("sarita_runtime/kernel/universal_governance/GUGI_TRACEABILITY_REPORT.md", "w") as f:
            f.write("# GUGI TRACEABILITY REPORT\n\n")
            f.write(f"- **Certified GUGI**: {report['certified_gugi']:.4f}\n")
            f.write(f"- **Reconstructed GUGI**: {report['reconstructed_gugi']:.4f}\n")
            f.write(f"- **Traceability Status**: {'PASSED' if report['is_traceable'] else 'FAILED'}\n")
            f.write(f"- **Consistency Status**: {'PASSED' if report['is_consistent'] else 'FAILED'}\n")
            f.write(f"- **Final Audit Status**: {report['status']}\n")
