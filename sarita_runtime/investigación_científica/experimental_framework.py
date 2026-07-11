import uuid
import datetime

class ScientificExperiment:
    """
    Core data structure representing a Scientific Experiment with permanent scientific UUID.
    """
    def __init__(self, name: str, description: str, hypothesis_id: str = None):
        self.experiment_id = f"EXP-UUID-{uuid.uuid4().hex.upper()}"
        self.name = name
        self.description = description
        self.hypothesis_id = hypothesis_id
        self.created_at = datetime.datetime.now(datetime.timezone.utc).isoformat()

        self.variables = {
            "independent": [],
            "dependent": [],
            "control": []
        }
        self.groups = {
            "control_group": None,
            "experimental_groups": []
        }
        self.protocols = []
        self.results = []
        self.replications = []
        self.metadata = {}
        self.traceability_chain = []
        self.status = "CREATED"  # CREATED, SCHEDULED, RUNNING, COMPLETED, VALIDATED, ARCHIVED

    def add_variable(self, var_type: str, name: str, val_range_or_val):
        if var_type in self.variables:
            self.variables[var_type].append({"name": name, "value": val_range_or_val})

    def to_dict(self) -> dict:
        return {
            "experiment_id": self.experiment_id,
            "name": self.name,
            "description": self.description,
            "hypothesis_id": self.hypothesis_id,
            "created_at": self.created_at,
            "variables": self.variables,
            "groups": self.groups,
            "protocols": self.protocols,
            "results": self.results,
            "replications": self.replications,
            "metadata": self.metadata,
            "traceability_chain": self.traceability_chain,
            "status": self.status
        }
