class KnowledgeQueryEngine:
    """
    Executes search and traversal queries across nodes and relationships.
    """
    def __init__(self, graph):
        self.graph = graph

    def find_nodes(self, node_type: str = None, properties: dict = None) -> list:
        nodes = list(self.graph.nodes.values())
        if node_type:
            nodes = [n for n in nodes if n.node_type == node_type]
        if properties:
            for k, v in properties.items():
                nodes = [n for n in nodes if n.properties.get(k) == v]
        return nodes

    def find_neighbors(self, node_id: str, relationship: str = None) -> list:
        neighbors = []
        for edge in self.graph.edges:
            if edge.source_id == node_id:
                if not relationship or edge.rel_type == relationship:
                    neighbors.append(self.graph.nodes.get(edge.target_id))
        return [n for n in neighbors if n is not None]
