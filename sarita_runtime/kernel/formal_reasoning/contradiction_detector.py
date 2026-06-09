class ContradictionDetector:
    """
    Detects logical contradictions within a set of expressions.
    """
    def __init__(self, reasoner):
        self.reasoner = reasoner

    def find_contradictions(self, expressions):
        from .logical_expression import LogicalExpression
        contradictions = []
        knowledge = list(expressions)

        # 1. Expand knowledge: decompose ANDs and literals
        expanded_knowledge = []
        queue = list(knowledge)
        while queue:
            p = queue.pop(0)
            if p not in expanded_knowledge:
                expanded_knowledge.append(p)
            if isinstance(p, LogicalExpression) and p.operator == "AND":
                queue.append(p.left)
                queue.append(p.right)

        # 2. Direct Contradictions (A and ~A) in expanded set
        for i, p1 in enumerate(expanded_knowledge):
            for p2 in expanded_knowledge[i+1:]:
                if isinstance(p1, LogicalExpression) and p1.operator == "NOT" and p1.left == p2:
                    contradictions.append(f"Contradiction: {p1} vs {p2}")
                elif isinstance(p2, LogicalExpression) and p2.operator == "NOT" and p2.left == p1:
                    contradictions.append(f"Contradiction: {p2} vs {p1}")

        if contradictions:
            return contradictions

        # 3. Derived Contradictions: Prove ~p from S\{p}
        # In the specific case of (P -> Q) and (P AND ~Q),
        # expanded knowledge already has P and ~Q.
        # We need to derive Q from others ([P->Q]) + P to hit direct contradiction.

        for p in expanded_knowledge:
            neg_p = LogicalExpression(p, "NOT")
            # others are all expanded facts except p and its parents
            others = [expr for expr in expanded_knowledge if expr != p]

            chain = self.reasoner.derive(others, neg_p)
            if chain:
                contradictions.append({
                    "type": "DERIVED_CONTRADICTION",
                    "premise": str(p),
                    "derivation": chain
                })

        return contradictions
