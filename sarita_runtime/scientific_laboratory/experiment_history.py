class ExperimentHistory:
    """
    Maintains a historical record of all completed scientific trials.
    """
    def __init__(self):
        self.history = []

    def log_trial(self, trial_data: dict):
        self.history.append(trial_data)

    def get_history(self) -> list:
        return self.history
