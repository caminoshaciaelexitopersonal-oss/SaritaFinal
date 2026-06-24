class CollapseDetector:
    def __init__(self, resource_manager):
        self.resource_manager = resource_manager

    def check_collapse_risk(self, civ):
        civ_id = civ["identity"]["id"]
        resources = self.resource_manager.get_resources(civ_id)

        # Collapse risk increases if resources are low
        risk = 0.0
        if resources < 10.0:
            risk = 0.8
        elif resources < 30.0:
            risk = 0.4

        return risk
