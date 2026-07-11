class KernelDirectory:
    """
    Directory of physical file structures, directories, and namespaces of the Sovereign Kernel.
    """
    def __init__(self):
        self.directories = {
            "root": "sarita_runtime/kernel/",
            "event_bus": "sarita_runtime/kernel/event_bus/",
            "state_manager": "sarita_runtime/kernel/state_manager/",
            "knowledge_graph": "sarita_runtime/kernel/knowledge_graph/",
            "autonomous_operation": "sarita_runtime/kernel/autonomous_operation/"
        }

    def get_path(self, key: str) -> str:
        return self.directories.get(key, "")
