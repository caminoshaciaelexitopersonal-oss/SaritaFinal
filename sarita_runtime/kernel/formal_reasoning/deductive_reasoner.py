from .logical_expression import LogicalExpression

class DeductiveReasoner:
    """
    Implements formal deduction rules: Modus Ponens, Modus Tollens, etc.
    Utilizes a TruthEvaluationEngine for secondary verification of derivations.
    """
    def __init__(self, truth_engine):
        self.truth_engine = truth_engine

    def derive(self, premises, goal_expr) -> list:
        """
        Performs step-by-step deduction. Returns the chain of inferences.
        Each inference is cross-checked against the TruthEvaluationEngine.
        """
        inferences = []
        current_knowledge = list(premises)

        # Simple BFS-like inference for Phase 101
        added_new = True
        limit = 10 # Search limit
        cycles = 0
        while added_new and cycles < limit:
            cycles += 1
            added_new = False
            new_knowledge = []

            # 1. Modus Ponens: A, A -> B => B
            for p1 in current_knowledge:
                for p2 in current_knowledge:
                    if not isinstance(p2, LogicalExpression):
                        continue
                    if p2.operator == "IMPLIES" and p2.left == p1:
                        if p2.right not in current_knowledge and p2.right not in new_knowledge:
                            # Secondary Truth Verification
                            if self._verify_inference([p1, p2], p2.right):
                                new_knowledge.append(p2.right)
                                inferences.append({
                                    "rule": "MODUS_PONENS",
                                    "premises": [str(p1), str(p2)],
                                    "conclusion": str(p2.right)
                                })
                                added_new = True

            # 2. Modus Tollens: A -> B, ~B => ~A
            for p1 in current_knowledge:
                for p2 in current_knowledge:
                    if not isinstance(p2, LogicalExpression):
                        continue
                    if p2.operator == "IMPLIES":
                        # Check for ~B (p1 is (NOT, p2.right))
                        if isinstance(p1, LogicalExpression) and p1.operator == "NOT" and p1.left == p2.right:
                            neg_a = LogicalExpression(p2.left, "NOT")
                            if neg_a not in current_knowledge and neg_a not in new_knowledge:
                                if self._verify_inference([p1, p2], neg_a):
                                    new_knowledge.append(neg_a)
                                    inferences.append({
                                        "rule": "MODUS_TOLLENS",
                                        "premises": [str(p1), str(p2)],
                                        "conclusion": str(neg_a)
                                    })
                                    added_new = True

            # 3. Hypothetical Syllogism: A -> B, B -> C => A -> C
            for p1 in current_knowledge:
                for p2 in current_knowledge:
                    if not isinstance(p1, LogicalExpression) or not isinstance(p2, LogicalExpression):
                        continue
                    if p1.operator == "IMPLIES" and p2.operator == "IMPLIES" and p1.right == p2.left:
                        implication = LogicalExpression(p1.left, "IMPLIES", p2.right)
                        if implication not in current_knowledge and implication not in new_knowledge:
                            if self._verify_inference([p1, p2], implication):
                                new_knowledge.append(implication)
                                inferences.append({
                                    "rule": "HYPOTHETICAL_SYLLOGISM",
                                    "premises": [str(p1), str(p2)],
                                    "conclusion": str(implication)
                                })
                                added_new = True

            # 4. Resolution: A v B, ~A => B
            for p1 in current_knowledge:
                for p2 in current_knowledge:
                    if not isinstance(p1, LogicalExpression):
                        continue
                    if p1.operator == "OR":
                        # Case 1: p2 is ~p1.left
                        if isinstance(p2, LogicalExpression) and p2.operator == "NOT" and p2.left == p1.left:
                            if p1.right not in current_knowledge and p1.right not in new_knowledge:
                                if self._verify_inference([p1, p2], p1.right):
                                    new_knowledge.append(p1.right)
                                    inferences.append({
                                        "rule": "RESOLUTION",
                                        "premises": [str(p1), str(p2)],
                                        "conclusion": str(p1.right)
                                    })
                                    added_new = True
                        # Case 2: p2 is ~p1.right
                        elif isinstance(p2, LogicalExpression) and p2.operator == "NOT" and p2.left == p1.right:
                            if p1.left not in current_knowledge and p1.left not in new_knowledge:
                                if self._verify_inference([p1, p2], p1.left):
                                    new_knowledge.append(p1.left)
                                    inferences.append({
                                        "rule": "RESOLUTION",
                                        "premises": [str(p1), str(p2)],
                                        "conclusion": str(p1.left)
                                    })
                                    added_new = True

            # Special Rule for AND decomposition
            for p in current_knowledge:
                if isinstance(p, LogicalExpression) and p.operator == "AND":
                    if p.left not in current_knowledge and p.left not in new_knowledge:
                        new_knowledge.append(p.left)
                        inferences.append({
                            "rule": "AND_DECOMPOSITION_LEFT",
                            "premises": [str(p)],
                            "conclusion": str(p.left)
                        })
                        added_new = True
                    if p.right not in current_knowledge and p.right not in new_knowledge:
                        new_knowledge.append(p.right)
                        inferences.append({
                            "rule": "AND_DECOMPOSITION_RIGHT",
                            "premises": [str(p)],
                            "conclusion": str(p.right)
                        })
                        added_new = True

            current_knowledge.extend(new_knowledge)

            # Check if goal is reached
            if any(k == goal_expr for k in current_knowledge):
                return inferences

        return [] # Could not derive goal

    def _verify_inference(self, premises, conclusion):
        """
        Cross-checks an inference step using the TruthEvaluationEngine.
        Ensures the conclusion is true in all models where premises are true.
        """
        # Collect all atomic variables
        atomics = set()
        for p in premises:
            atomics.update(self._get_atomics(p))
        atomics.update(self._get_atomics(conclusion))

        # Generate truth table for (P1 AND P2 ... PN) -> C
        import itertools
        atomics_list = list(atomics)
        for values in itertools.product([False, True], repeat=len(atomics_list)):
            context = dict(zip(atomics_list, values))

            # If all premises are true
            all_p_true = all(self.truth_engine.evaluate(p, context) for p in premises)
            if all_p_true:
                # Then conclusion must also be true
                if not self.truth_engine.evaluate(conclusion, context):
                    return False

        return True

    def _get_atomics(self, expr):
        if not isinstance(expr, LogicalExpression):
            return {str(expr)}
        atomics = set()
        atomics.update(self._get_atomics(expr.left))
        if expr.right is not None:
            atomics.update(self._get_atomics(expr.right))
        return atomics
