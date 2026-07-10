import collections

class CapabilityGraph:
    """
    Maintains a dependency structure mapping relationship dependencies between capabilities.
    """
    def __init__(self):
        self.nodes = set()
        self.edges = collections.defaultdict(list)

    def add_node(self, node: str):
        self.nodes.add(node)

    def add_dependency(self, from_node: str, to_node: str):
        self.edges[from_node].append(to_node)
        self.nodes.add(from_node)
        self.nodes.add(to_node)

    def to_dict(self) -> dict:
        return {
            "nodes": list(self.nodes),
            "dependencies": {k: v for k, v in self.edges.items()}
        }
