class KnowledgeVisualizer:
    """
    Renders human-readable ASCII representations and layouts of graph relationships.
    """
    def __init__(self, graph):
        self.graph = graph

    def render_ascii_map(self) -> str:
        """
        Renders an ASCII mapping of current graph topology and core layers.
        """
        lines = []
        lines.append("=== SARITA KNOWLEDGE GRAPH TOPOLOGY ===")
        lines.append(f"Active Nodes: {len(self.graph.nodes)} | Edges: {len(self.graph.edges)}")
        lines.append("--------------------------------------")

        # Render a simple hierarchical layout of nodes grouped by types
        by_type = {}
        for node in self.graph.nodes.values():
            by_type.setdefault(node.node_type, []).append(node.node_id)

        for ntype, ids in by_type.items():
            lines.append(f"Layer [{ntype.upper()}]:")
            for nid in ids[:10]: # Limit print to 10 nodes for clean spacing
                lines.append(f"  └─ {nid}")
                # Find targets
                targets = []
                for edge in self.graph.edges:
                    if edge.source_id == nid:
                        targets.append(f"{edge.rel_type}->{edge.target_id}")
                if targets:
                    lines.append(f"       ({', '.join(targets)})")

        lines.append("=======================================")
        return "\n".join(lines)
