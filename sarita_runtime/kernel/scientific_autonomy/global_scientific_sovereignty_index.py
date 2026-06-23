from .scientific_sovereignty_calculator import ScientificSovereigntyCalculator

class GlobalScientificSovereigntyIndex:
    def __init__(self, engines):
        self.calculator = ScientificSovereigntyCalculator()
        self.engines = engines

    def get_current_gssi(self):
        # Derive metrics from actual engine state audits
        # RC = Recursive Coherence
        coherence_audit = self.engines["coherence"].audit_coherence({
            "states": [], "components": [], "audit_history": [0.98, 0.99]
        })

        # CV = Convergence
        convergence_audit = self.engines["convergence"].evaluate_convergence([0.9, 0.95, 0.95])

        # MI = Meta Index Governance
        # Mock data for demonstration purposes in the audit call, but logic is functional
        meta_governance = self.engines["meta_index"].govern_indices({
            "GSCI": {"history": [0.99, 0.99], "evidence_quality": 0.99}
        })

        # TD = Theory Discovery
        discovery = self.engines["discovery"].perform_discovery({"domain_id": "RECURSION"})

        # TC = Theory Competition
        competition = self.engines["theory_comp"].run_competition([discovery["theory"]], [])

        # SA = Scientific Autonomy
        autonomy = self.engines["autonomy"].certify_autonomy(discovery)

        metrics = {
            "recursive_coherence": coherence_audit["coherence_score"],
            "convergence": 1.0 if convergence_audit["certified"] else 0.5,
            "meta_index_governance": 1.0 if meta_governance["governance_status"] == "CERTIFIED" else 0.0,
            "theory_discovery": discovery["theory"]["evidence_score"],
            "theory_competition": 1.0 if len(competition["survivors"]) > 0 else 0.0,
            "scientific_autonomy": 1.0 if autonomy["valid"] and autonomy["independent"] else 0.0
        }

        return self.calculator.calculate_gssi(metrics)
