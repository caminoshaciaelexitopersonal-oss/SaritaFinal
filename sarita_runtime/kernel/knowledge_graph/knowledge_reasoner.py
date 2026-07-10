class KnowledgeReasoner:
    """
    Deductive inference processor that derives logical implications,
    uncovers indirect risks, and validates relational integrity.
    """
    def __init__(self, graph):
        self.graph = graph

    def infer_risk_propagation(self) -> list:
        """
        Infers transitive risks.
        If engine A depends on engine B, and B is flagged high-risk, A inherits risk warnings.
        """
        warnings = []
        for edge in self.graph.edges:
            if edge.rel_type == "depends_on":
                source_node = self.graph.nodes.get(edge.source_id)
                target_node = self.graph.nodes.get(edge.target_id)
                if source_node and target_node:
                    target_risk = target_node.properties.get("risk_level", 0.0)
                    if target_risk > 0.5:
                        warnings.append({
                            "derived_fact": f"Risk propagated to {source_node.node_id} from {target_node.node_id}",
                            "severity": "MEDIUM"
                        })
        return warnings
