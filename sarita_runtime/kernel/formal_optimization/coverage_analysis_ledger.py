from .optimality_ledger import OptimalityLedger

class CoverageAnalysisLedger(OptimalityLedger):
    """
    Ledger for recording axiomatic coverage audits and gap detections.
    """
    def record_coverage_audit(self, coverage_report):
        entry = {
            "type": "COVERAGE_AUDIT",
            "coverage_ratio": coverage_report["coverage_ratio"],
            "gaps_count": len(coverage_report["uncovered_scenarios"]),
            "timestamp": time.time()
        }
        self._write(entry)
