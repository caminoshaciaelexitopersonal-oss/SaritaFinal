import collections

class KnowledgeIndexer:
    """
    Maintains active inverted indexes of KnowledgeNode types and property keywords.
    """
    def __init__(self):
        self.type_index = collections.defaultdict(set)

    def index_node(self, node):
        self.type_index[node.node_type].add(node.node_id)

    def deindex_node(self, node):
        if node.node_id in self.type_index[node.node_type]:
            self.type_index[node.node_type].remove(node.node_id)

    def get_by_type(self, node_type: str) -> set:
        return self.type_index.get(node_type, set())
