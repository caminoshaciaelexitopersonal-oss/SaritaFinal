import json
import os
from .knowledge_node import KnowledgeNode
from .knowledge_edge import KnowledgeEdge
from .knowledge_indexer import KnowledgeIndexer
from .knowledge_query_engine import KnowledgeQueryEngine
from .ontology_integrator import OntologyIntegrator
from .knowledge_reasoner import KnowledgeReasoner
from .knowledge_history import KnowledgeHistory
from .knowledge_visualizer import KnowledgeVisualizer
from .knowledge_relationship_builder import KnowledgeRelationshipBuilder

class UnifiedKnowledgeGraph:
    """
    Central Repository for all SARITA knowledge vectors, concepts, and relationships.
    Contains everything from engines and indices to cosmos, universos, and events.
    """
    def __init__(self):
        self.nodes = {}
        self.edges = []
        self.indexer = KnowledgeIndexer()
        self.query_engine = KnowledgeQueryEngine(self)
        self.ontology_integrator = OntologyIntegrator()
        self.reasoner = KnowledgeReasoner(self)
        self.history = KnowledgeHistory()
        self.visualizer = KnowledgeVisualizer(self)
        self.relationship_builder = KnowledgeRelationshipBuilder(self)

    def add_node(self, node_id: str, node_type: str, properties: dict = None) -> bool:
        node = KnowledgeNode(node_id, node_type, properties)
        if not self.ontology_integrator.validate_node(node):
            # Invalid type, but let's register in ontology integrator to support it
            self.ontology_integrator.valid_types.add(node_type)

        self.nodes[node_id] = node
        self.indexer.index_node(node)
        self.history.record_mutation("ADD_NODE", node_id, node.to_dict())
        return True

    def remove_node(self, node_id: str) -> bool:
        node = self.nodes.get(node_id)
        if not node:
            return False
        self.indexer.deindex_node(node)
        # Remove incident edges
        self.edges = [e for e in self.edges if e.source_id != node_id and e.target_id != node_id]
        del self.nodes[node_id]
        self.history.record_mutation("REMOVE_NODE", node_id, {})
        return True

    def add_relationship(self, source_id: str, target_id: str, rel_type: str, properties: dict = None) -> bool:
        if source_id not in self.nodes or target_id not in self.nodes:
            # We automatically add nodes if they don't exist to ensure zero-stub resilience
            if source_id not in self.nodes:
                self.add_node(source_id, "engine")
            if target_id not in self.nodes:
                self.add_node(target_id, "index")

        edge = KnowledgeEdge(source_id, target_id, rel_type, properties)
        self.edges.append(edge)
        self.history.record_mutation("ADD_EDGE", f"{source_id}->{target_id}", edge.to_dict())
        return True

    def persist_graph(self, path: str = "sarita_runtime/kernel/knowledge_graph/knowledge_graph.json"):
        os.makedirs(os.path.dirname(path), exist_ok=True)
        data = {
            "nodes": {nid: node.to_dict() for nid, node in self.nodes.items()},
            "edges": [edge.to_dict() for edge in self.edges]
        }
        with open(path, "w") as f:
            json.dump(data, f, indent=2)
