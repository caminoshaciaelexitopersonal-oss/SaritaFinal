import math

class ErrorPropagationEngine:
    """
    Computes mathematical propagation of measurement and statistical errors through calculations (e.g. addition, division).
    """
    def __init__(self):
        pass

    def propagate_addition(self, error_a: float, error_b: float) -> float:
        return round(math.sqrt(error_a**2 + error_b**2), 4)

    def propagate_multiplication(self, val_a: float, error_a: float, val_b: float, error_b: float) -> float:
        if val_a == 0 or val_b == 0:
            return 0.0
        rel_a = error_a / abs(val_a)
        rel_b = error_b / abs(val_b)
        rel_total = math.sqrt(rel_a**2 + rel_b**2)
        product = val_a * val_b
        return round(rel_total * abs(product), 4)
