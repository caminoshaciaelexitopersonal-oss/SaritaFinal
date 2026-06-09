class LogicalOperatorRegistry:
    """
    Registry for supported logical operators and their implementations.
    """
    def __init__(self):
        self.operators = {
            "AND": lambda a, b: a and b,
            "OR": lambda a, b: a or b,
            "NOT": lambda a: not a,
            "XOR": lambda a, b: a != b,
            "IMPLIES": lambda a, b: (not a) or b,
            "IFF": lambda a, b: a == b
        }

    def get_operator(self, name):
        op = self.operators.get(name)
        if not op:
            raise ValueError(f"Operator {name} not supported.")
        return op
