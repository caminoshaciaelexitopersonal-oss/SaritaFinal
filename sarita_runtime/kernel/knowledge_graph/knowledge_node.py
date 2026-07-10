class KnowledgeNode:
    """
    Represents a specific ontological concept or system component in the Unified Knowledge Graph.
    """
    def __init__(self, node_id: str, node_type: str, properties: dict = None):
        self.node_id = node_id
        self.node_type = node_type
        self.properties = properties or {}

    def to_dict(self) -> dict:
        return {
            "node_id": self.node_id,
            "node_type": self.node_type,
            "properties": self.properties
        }
