class KnowledgeEdge:
    """
    Represents a typed relationship edge between two ontological nodes in the Graph.
    """
    def __init__(self, source_id: str, target_id: str, rel_type: str, properties: dict = None):
        self.source_id = source_id
        self.target_id = target_id
        self.rel_type = rel_type
        self.properties = properties or {}

    def to_dict(self) -> dict:
        return {
            "source_id": self.source_id,
            "target_id": self.target_id,
            "relationship": self.rel_type,
            "properties": self.properties
        }
