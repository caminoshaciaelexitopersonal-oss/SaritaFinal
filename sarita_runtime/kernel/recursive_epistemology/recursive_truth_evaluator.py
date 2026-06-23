class RecursiveTruthEvaluator:
    def evaluate(self, truth_claim, depth=1):
        # Evaluates a truth claim with recursive depth
        base_validity = 0.95
        recursion_penalty = 0.01 * depth
        return max(0.0, base_validity - recursion_penalty)
