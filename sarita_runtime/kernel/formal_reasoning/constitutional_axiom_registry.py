from .logical_expression import LogicalExpression

class ConstitutionalAxiomRegistry:
    """
    Registry for foundational constitutional axioms.
    """
    def __init__(self, detector):
        self.detector = detector
        self.axioms = {}
        self._initialize_core_axioms()

    def _initialize_core_axioms(self):
        # 1. Axiom of Identity: Identity must be preserved across transitions.
        self.register_axiom("AX-IDENTITY", LogicalExpression("IDENTITY_VALID", "IMPLIES", "SOVEREIGN_ID"))

        # 2. Axiom of Purpose: Evolution must align with foundational intent.
        self.register_axiom("AX-PURPOSE", LogicalExpression("PURPOSE_ALIGNED", "IMPLIES", "CONSTITUTIONAL_VALIDITY"))

        # 3. Axiom of Continuity: State transitions must be causally linked.
        self.register_axiom("AX-CONTINUITY", LogicalExpression("CAUSAL_PARENT_EXISTS", "AND", "HASH_INTEGRITY"))

        # 4. Axiom of Legitimacy: Survival depends on existential justification.
        self.register_axiom("AX-LEGITIMACY", LogicalExpression("EXISTENTIAL_BENEFIT", "AND", "CONSTITUTIONAL_NECESSITY"))

        # 5. Axiom of Governance: All actions must be authorized by the Unified Graph.
        self.register_axiom("AX-GOVERNANCE", LogicalExpression("GRAPH_AUTHORIZED", "IFF", "SOVEREIGN_ACTION"))

    def register_axiom(self, axiom_id, expression):
        # Check for conflicts using the detector directly
        current_axioms = list(self.axioms.values())
        if self.detector.find_contradictions(current_axioms + [expression]):
            return False

        self.axioms[axiom_id] = expression
        return True

    def get_all_axioms(self):
        return list(self.axioms.values())
