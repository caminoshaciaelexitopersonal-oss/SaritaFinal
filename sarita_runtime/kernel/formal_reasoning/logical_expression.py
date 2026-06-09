class LogicalExpression:
    """
    Represents a formal logical expression.
    """
    def __init__(self, left, operator, right=None):
        self.left = left
        self.operator = operator
        self.right = right

    def __repr__(self):
        if self.right is not None:
            return f"({self.left} {self.operator} {self.right})"
        return f"({self.operator} {self.left})"

    def to_dict(self):
        return {
            "left": self.left,
            "operator": self.operator,
            "right": self.right
        }

    def __eq__(self, other):
        if not isinstance(other, LogicalExpression):
            return False
        return (self.left == other.left and
                self.operator == other.operator and
                self.right == other.right)

    def __hash__(self):
        return hash((self.left, self.operator, self.right))
