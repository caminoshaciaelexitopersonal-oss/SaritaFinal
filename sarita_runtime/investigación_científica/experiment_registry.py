from .experimental_framework import ScientificExperiment

class ExperimentRegistry:
    """
    Registry database/storage layer for all recorded scientific experiments.
    """
    def __init__(self):
        self.experiments = {}

    def register(self, experiment: ScientificExperiment):
        self.experiments[experiment.experiment_id] = experiment

    def get(self, experiment_id: str) -> ScientificExperiment:
        return self.experiments.get(experiment_id)

    def update(self, experiment: ScientificExperiment):
        self.experiments[experiment.experiment_id] = experiment

    def list_all(self) -> list:
        return list(self.experiments.values())

    def clear(self):
        self.experiments.clear()
