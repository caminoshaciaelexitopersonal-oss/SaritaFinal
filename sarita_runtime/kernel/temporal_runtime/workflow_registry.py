class WorkflowRegistry:
    def __init__(self):
        self.workflows = ["FinancialSaga", "BookingSaga", "AuditMission"]

    def get_workflows(self):
        return self.workflows
