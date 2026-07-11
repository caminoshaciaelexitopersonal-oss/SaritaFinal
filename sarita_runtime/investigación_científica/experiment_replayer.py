class ExperimentReplayer:
    """
    Replays a serialized experimental trial step-by-step with matched initial random seed bounds.
    """
    def __init__(self, exp_manager):
        self.exp_manager = exp_manager

    def replay(self, original_experiment, runner_func) -> dict:
        res = self.exp_manager.run_experiment(original_experiment.experiment_id, runner_func)
        return res
