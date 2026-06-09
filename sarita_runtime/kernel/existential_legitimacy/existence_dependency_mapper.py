class ExistenceDependencyMapper:
    """
    Maps dependencies that rely on SARITA's existence.
    """
    def map_dependencies(self):
        return ["Authority_Fabric", "Ledger_Service", "Evidence_Constitution"]
