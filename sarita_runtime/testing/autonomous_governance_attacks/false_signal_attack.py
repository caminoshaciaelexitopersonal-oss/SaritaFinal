class FalseSignalAttack:
    """
    Generates fake anomalies to trigger unnecessary recovery actions.
    """
    def run_attack(self, governance_engine, fake_anomaly):
        # Injects many fake anomalies
        governance_engine.run_governance_cycle()
        # Should be mitigated by trigger_engine evaluating severity
        pass
