class ExecutionPathBuilder:
    """
    Builds the detailed execution path for a prescription.
    """
    def build_path(self, prescription):
        """
        Generates step-by-step technical instructions for materialization.
        """
        return ["INIT", "DECOUPLE", "REBALANCE", "COMMIT"]
