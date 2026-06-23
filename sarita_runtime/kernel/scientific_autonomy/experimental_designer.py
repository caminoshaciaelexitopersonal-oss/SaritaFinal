class ExperimentalDesigner:
    def design_experiment(self, hypothesis):
        # Designs a protocol to validate or refute a hypothesis
        return {
            "hypothesis_id": hypothesis["id"],
            "protocol": "RECURSIVE_STRESS_TEST",
            "sample_size": 1000000
        }
