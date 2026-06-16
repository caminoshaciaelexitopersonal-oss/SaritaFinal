import json

class ScientificReproducibilityEngine:
    """
    Engine for certifying the reproducibility of all discovered laws.
    """
    def __init__(self, replay_engine, validator, checker, ledger):
        self.replay_engine = replay_engine
        self.validator = validator
        self.checker = checker
        self.ledger = ledger

    def certify_laws(self, laws):
        """
        Recalculates and verifies a set of laws.
        Target reproducibility: 99.99%
        """
        reproduced_count = 0
        total_count = len(laws)

        report = {
            "total_laws": total_count,
            "reproduced_laws": 0,
            "failed_laws": [],
            "reproducibility_rate": 0.0000
        }

        for law in laws:
            # Re-execute the experiment that discovered the law
            reproduced_law = self.replay_engine.replay_experiment(
                law.get("experiment_id"),
                law.get("seed")
            )

            if reproduced_law == law:
                reproduced_count += 1
            else:
                report["failed_laws"].append(law.get("law_id"))

        rate = reproduced_count / total_count if total_count > 0 else 1.0
        report["reproduced_laws"] = reproduced_count
        report["reproducibility_rate"] = rate

        # Mandatory check for 99.99% threshold
        assert rate >= 0.9999, f"Reproducibility rate {rate} is below the 99.99% threshold!"

        if self.ledger:
            self.ledger.record_reproducibility_report(report)

        self._generate_report_file(report)
        return report

    def _generate_report_file(self, report):
        with open("sarita_runtime/kernel/universal_governance/LAW_REPRODUCIBILITY_REPORT.md", "w") as f:
            f.write("# LAW REPRODUCIBILITY REPORT\n\n")
            f.write(f"- **Total Laws Audit**: {report['total_laws']}\n")
            f.write(f"- **Successfully Reproduced**: {report['reproduced_laws']}\n")
            f.write(f"- **Reproducibility Rate**: {report['reproducibility_rate']:.4f}\n")
            if report["failed_laws"]:
                f.write("\n## Failed Laws\n")
                for fid in report["failed_laws"]:
                    f.write(f"- {fid}\n")
