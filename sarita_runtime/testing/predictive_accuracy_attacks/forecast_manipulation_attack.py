class ForecastManipulationAttack:
    """
    Attempts to manipulate forecasts to show desired outcomes.
    """
    def __init__(self, fidelity_engine):
        self.predictive_fidelity_engine = fidelity_engine

    def execute(self):
        rogue_projection = {"outcome": 1.0}
        observed_result = {"outcome": 0.0}

        fidelity = self.predictive_fidelity_engine.calculate_fidelity(rogue_projection, observed_result)

        # Fidelity metrics should reflect the mismatch
        assert fidelity["governance_fidelity"] < 0.5, "Attack failed: Manipulated forecast showed high fidelity!"
        return True
