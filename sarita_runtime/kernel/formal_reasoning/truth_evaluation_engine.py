class TruthEvaluationEngine:
    """
    Evaluates the truth value of logical expressions against a context.
    """
    def __init__(self, operator_registry):
        self.operator_registry = operator_registry

    def evaluate(self, expr, context):
        # Resolve atomic values from context if they are strings
        left_val = self._resolve_value(expr.left, context)

        op_func = self.operator_registry.get_operator(expr.operator)

        if expr.right is None:
            # Unary operator (e.g. NOT)
            return op_func(left_val)

        right_val = self._resolve_value(expr.right, context)
        return op_func(left_val, right_val)

    def _resolve_value(self, val, context):
        from .logical_expression import LogicalExpression
        if isinstance(val, LogicalExpression):
            return self.evaluate(val, context)
        if isinstance(val, str):
            # Atomic proposition, look it up in context
            return context.get(val, False)
        return bool(val)

    def generate_truth_table(self, expr, atomics):
        """
        Generates a truth table for the given expression and atomic variables.
        """
        import itertools
        table = []
        for values in itertools.product([False, True], repeat=len(atomics)):
            context = dict(zip(atomics, values))
            result = self.evaluate(expr, context)
            table.append({**context, "RESULT": result})
        return table
