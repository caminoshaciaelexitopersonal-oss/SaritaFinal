class ExperimentRegistry:
    """
    Registry for cataloging experimental schemas and variables.
    """
    def __init__(self):
        self._experiments = {}

    def register_experiment(self, exp_id: str, metadata: dict):
        self._experiments[exp_id] = metadata

    def get_experiment(self, exp_id: str) -> dict:
        return self._experiments.get(exp_id, {})

    def list_experiments(self) -> list:
        return list(self._experiments.keys())
