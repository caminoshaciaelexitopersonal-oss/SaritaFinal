class FormalLogicCore:
    """
    Core engine for handling formal logical operations and truth evaluation.
    """
    def __init__(self, operator_registry, evaluation_engine):
        self.operator_registry = operator_registry
        self.evaluation_engine = evaluation_engine

    def evaluate_expression(self, expression, context):
        return self.evaluation_engine.evaluate(expression, context)

    def is_consistent(self, expressions, context):
        """
        Verifies if a set of expressions can all be true simultaneously in the given context.
        """
        for expr in expressions:
            if not self.evaluate_expression(expr, context):
                return False
        return True
