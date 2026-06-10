from sarita_runtime.kernel.formal_reasoning.logical_expression import LogicalExpression

class AxiomCoverageAnalyzer:
    """
    Analyzes which axioms cover which scenarios using logical relevance.
    """
    def map_axioms_to_scenarios(self, axioms, scenarios):
        mapping = {}
        for axiom in axioms:
            axiom_id = str(axiom)
            mapping[axiom_id] = []
            for scenario in scenarios:
                if self._is_axiom_relevant(axiom, scenario):
                    mapping[axiom_id].append(scenario["id"])
        return mapping

    def _is_axiom_relevant(self, axiom, scenario):
        """
        Determines relevance based on the logical overlap between
        axiom atomic components and scenario tags.
        """
        # Collect all atomic symbols from the axiom expression
        atomics = self._get_atomics(axiom)
        scenario_tags = [t.upper() for t in scenario.get("tags", [])]

        # Relevance is confirmed if any atomic symbol matches a scenario tag
        for atomic in atomics:
            if atomic.upper() in scenario_tags:
                return True
        return False

    def _get_atomics(self, expr):
        atomics = set()
        if isinstance(expr.left, LogicalExpression):
            atomics.update(self._get_atomics(expr.left))
        elif isinstance(expr.left, str):
            atomics.add(expr.left)

        if isinstance(expr.right, LogicalExpression):
            atomics.update(self._get_atomics(expr.right))
        elif isinstance(expr.right, str):
            atomics.add(expr.right)
        return atomics
