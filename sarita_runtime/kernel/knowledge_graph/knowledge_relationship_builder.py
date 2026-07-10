from .knowledge_edge import KnowledgeEdge

class KnowledgeRelationshipBuilder:
    """
    Automates semantic connection wiring across registered modules, APIs, and events.
    """
    def __init__(self, graph):
        self.graph = graph

    def auto_wire_relationships(self):
        """
        Scans registered nodes and automatically links dependent modules.
        """
        engines = [nid for nid, node in self.graph.nodes.items() if node.node_type == "engine"]
        indices = [nid for nid, node in self.graph.nodes.items() if node.node_type == "index"]
        axioms = [nid for nid, node in self.graph.nodes.items() if node.node_type == "axiom"]

        # Link engines to indices they evaluate
        for eng in engines:
            for idx in indices:
                # If there's keyword matches (e.g., 'consistency' engine and 'consistency' index)
                # Or standard fallback wiring
                if any(kw in eng and kw in idx for kw in ["consistency", "operation", "governance", "learning"]):
                    self.graph.add_relationship(eng, idx, "evaluates")

        # Link indices to axioms they validate
        for idx in indices:
            for ax in axioms:
                self.graph.add_relationship(idx, ax, "validates")
