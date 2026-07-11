import uuid
import math

class DecisionNode:
    """
    Represents a specific decision node in the autonomous decision tree.
    """
    def __init__(self, node_id, description, evidence, hypothesis, alternatives, priority=0.5):
        self.node_id = node_id or str(uuid.uuid4())
        self.description = description
        self.evidence = evidence
        self.hypothesis = hypothesis
        self.alternatives = alternatives or []
        self.priority = priority

        # Multi-criteria evaluations
        self.risk = 0.0
        self.benefit = 0.0
        self.uncertainty = 0.0
        self.impact = 0.0
        self.score = 0.0

        self.justification = ""
        self.result_expected = ""
        self.result_obtained = ""
        self.status = "PENDING"
        self.children = []

    def to_dict(self):
        return {
            "decision_id": self.node_id,
            "description": self.description,
            "evidence": self.evidence,
            "hypothesis": self.hypothesis,
            "risk": round(self.risk, 4),
            "benefit": round(self.benefit, 4),
            "uncertainty": round(self.uncertainty, 4),
            "priority": round(self.priority, 4),
            "impact": round(self.impact, 4),
            "score": round(self.score, 4),
            "alternatives": self.alternatives,
            "justification": self.justification,
            "result_expected": self.result_expected,
            "result_obtained": self.result_obtained,
            "status": self.status,
            "children": [child.to_dict() for child in self.children]
        }

class DecisionEngine:
    """
    Automated Decision Engine that evaluates multiple criteria to determine
    the optimal path of modification.
    """
    def __init__(self):
        self.root = None
        self.decisions_registry = {}

    def construct_decision_tree(self, proposals: list) -> DecisionNode:
        """
        Builds a structured decision tree from incoming architectural or operational proposals.
        """
        self.root = DecisionNode(
            node_id="ROOT-DECISION-DEC-001",
            description="System Autonomous Orchestration State Verification",
            evidence={"initial_state": "VERIFIED"},
            hypothesis="System is operational but can achieve higher efficiency via autonomous evolution",
            alternatives=["Do Nothing", "Simulate Evolution", "Execute Controlled Refactoring"]
        )
        self._evaluate_node(self.root)
        self.decisions_registry[self.root.node_id] = self.root

        for proposal in proposals:
            child = DecisionNode(
                node_id=proposal.get("id"),
                description=proposal.get("description", "Refactor Target"),
                evidence=proposal.get("evidence", {}),
                hypothesis=proposal.get("hypothesis", ""),
                alternatives=proposal.get("alternatives", []),
                priority=proposal.get("priority", 0.5)
            )
            self._evaluate_node(child, proposal)
            self.root.children.append(child)
            self.decisions_registry[child.node_id] = child

        return self.root

    def _evaluate_node(self, node: DecisionNode, proposal_data: dict = None):
        """
        Performs multi-criteria evaluation and score calculation.
        """
        if proposal_data:
            node.risk = float(proposal_data.get("risk", 0.3))
            node.benefit = float(proposal_data.get("benefit", 0.8))
            node.uncertainty = float(proposal_data.get("uncertainty", 0.2))
            node.impact = float(proposal_data.get("impact", 0.7))
        else:
            # Root or default values
            node.risk = 0.1
            node.benefit = 0.9
            node.uncertainty = 0.05
            node.impact = 0.95

        # Score calculation formula: Benefit * Impact * (1 - Risk) * (1 - Uncertainty * 0.5) * Priority
        node.score = (node.benefit * node.impact * (1.0 - node.risk) * (1.0 - node.uncertainty * 0.5) * node.priority)

        # Build justification based on mathematical dominance
        if node.score >= 0.4:
            node.justification = (
                f"Approved based on positive benefit-to-risk ratio. "
                f"Benefit ({node.benefit}) and Impact ({node.impact}) significantly outweigh Risk ({node.risk}) "
                f"with controlled uncertainty ({node.uncertainty})."
            )
            node.result_expected = "Successful structural and functional optimization yielding >5% GSAI increases."
        else:
            node.justification = f"Rejected due to unfavorable risk/uncertainty profile or low priority."
            node.result_expected = "Preservation of current stable system state."

    def execute_decision(self, node_id: str, success: bool, feedback: str = ""):
        """
        Applies result back to the decision node.
        """
        node = self.decisions_registry.get(node_id)
        if node:
            node.status = "EXECUTED" if success else "FAILED"
            node.result_obtained = feedback or ("Successfully optimized and verified." if success else "Failed verification or encountered rollback.")
            return node
        return None
