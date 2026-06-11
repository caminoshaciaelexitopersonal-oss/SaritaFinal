class TheoremLineageValidator:
    """
    Engine for validating the lineage of universal theorems.
    """
    def __init__(self, reconstructor, auditor, ledger):
        self.reconstructor = reconstructor
        self.auditor = auditor
        self.ledger = ledger

    def validate_theorems(self, theorems):
        """
        Verifies 25+ universal theorems by reconstructing their proofs.
        """
        report = {
            "total_theorems": len(theorems),
            "validated_theorems": 0,
            "failed_theorems": [],
            "reconstructions": []
        }

        for theorem in theorems:
            proof_chain = self.reconstructor.reconstruct_proof(theorem)
            is_valid, reason = self.auditor.audit_derivation(proof_chain)

            # Mandatory check: no uuid_only_proofs
            assert is_valid, f"Theorem {theorem.id} failed reconstruction: {reason}"

            if is_valid:
                report["validated_theorems"] += 1
                report["reconstructions"].append(proof_chain)
            else:
                report["failed_theorems"].append({"id": theorem.id, "reason": reason})

        if self.ledger:
            self.ledger.record_theorem_audit(report)

        self._generate_report_file(report)
        return report

    def _generate_report_file(self, report):
        with open("sarita_runtime/kernel/universal_governance/THEOREM_RECONSTRUCTION_REPORT.md", "w") as f:
            f.write("# THEOREM RECONSTRUCTION REPORT\n\n")
            f.write(f"- **Total Theorems Audit**: {report['total_theorems']}\n")
            f.write(f"- **Successfully Reconstructed**: {report['validated_theorems']}\n")
            f.write("\n## Validated Lineage Examples\n")
            for proof in report["reconstructions"][:5]: # Show first 5
                f.write(f"### Theorem: {proof['theorem_id']}\n")
                f.write(f"- **Axiom**: {proof['axiom']}\n")
                f.write(f"- **Law**: {proof['law']}\n")
                f.write(f"- **Steps**: {proof['inference_steps']}\n")
                f.write(f"- **Conclusion**: {proof['conclusion']}\n\n")
