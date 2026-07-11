import os
import json
import datetime
from .experimental_framework import ScientificExperiment

class ExperimentManager:
    """
    Manages the runtime execution, protocol attachments, lifecycle triggers, and persistency
    of scientific experiments.
    """
    def __init__(self, registry=None):
        self.registry = registry
        self.active_experiments = {}

    def create_experiment(self, name: str, description: str, hypothesis_id: str = None) -> ScientificExperiment:
        exp = ScientificExperiment(name, description, hypothesis_id)
        self.active_experiments[exp.experiment_id] = exp
        if self.registry:
            self.registry.register(exp)
        return exp

    def run_experiment(self, experiment_id: str, runner_func) -> dict:
        exp = self.active_experiments.get(experiment_id)
        if not exp:
            if self.registry:
                exp = self.registry.get(experiment_id)
            if not exp:
                raise ValueError(f"Experiment {experiment_id} not found.")

        exp.status = "RUNNING"
        start_time = datetime.datetime.now(datetime.timezone.utc).isoformat()
        exp.traceability_chain.append(f"Execution started at {start_time}")

        try:
            raw_results = runner_func(exp)
            exp.status = "COMPLETED"
            end_time = datetime.datetime.now(datetime.timezone.utc).isoformat()
            exp.traceability_chain.append(f"Execution completed successfully at {end_time}")

            exp.results.append({
                "run_id": len(exp.results) + 1,
                "timestamp": end_time,
                "data": raw_results,
                "status": "SUCCESS"
            })
            if self.registry:
                self.registry.update(exp)
            return {"status": "SUCCESS", "results": raw_results}
        except Exception as e:
            exp.status = "FAILED"
            fail_time = datetime.datetime.now(datetime.timezone.utc).isoformat()
            exp.traceability_chain.append(f"Execution failed at {fail_time} with error: {str(e)}")
            exp.results.append({
                "run_id": len(exp.results) + 1,
                "timestamp": fail_time,
                "error": str(e),
                "status": "FAILED"
            })
            if self.registry:
                self.registry.update(exp)
            return {"status": "FAILED", "error": str(e)}
