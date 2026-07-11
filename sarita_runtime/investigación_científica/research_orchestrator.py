class ResearchOrchestrator:
    """
    Orchestrates complex multi-hypothesis, multi-experiment scientific research campaigns.
    """
    def __init__(self, exp_manager, hypothesis_engine=None):
        self.exp_manager = exp_manager
        self.hypothesis_engine = hypothesis_engine
        self.campaigns = {}

    def create_campaign(self, name: str, description: str) -> dict:
        campaign_id = f"CAMPAIGN-{name.upper().replace(' ', '_')}"
        self.campaigns[campaign_id] = {
            "name": name,
            "description": description,
            "hypotheses": [],
            "experiments": [],
            "status": "INITIATED"
        }
        return self.campaigns[campaign_id]

    def add_hypothesis_to_campaign(self, campaign_id: str, hypothesis_id: str):
        if campaign_id in self.campaigns:
            self.campaigns[campaign_id]["hypotheses"].append(hypothesis_id)

    def add_experiment_to_campaign(self, campaign_id: str, experiment_id: str):
        if campaign_id in self.campaigns:
            self.campaigns[campaign_id]["experiments"].append(experiment_id)

    def execute_campaign(self, campaign_id: str, runners_map: dict) -> dict:
        campaign = self.campaigns.get(campaign_id)
        if not campaign:
            raise ValueError(f"Campaign {campaign_id} not found.")

        campaign["status"] = "RUNNING"
        results = {}
        for exp_id in campaign["experiments"]:
            runner = runners_map.get(exp_id)
            if runner:
                res = self.exp_manager.run_experiment(exp_id, runner)
                results[exp_id] = res
            else:
                results[exp_id] = {"status": "SKIPPED", "reason": "No runner mapped"}

        campaign["status"] = "COMPLETED"
        return results
