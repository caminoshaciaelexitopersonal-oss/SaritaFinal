class DominanceValidator:
    """
    Mathematically validates that solution A dominates solution B.
    """
    def validate_dominance(self, sol_a, sol_b, objectives):
        better_in_all = all(sol_a.get(obj, 0) >= sol_b.get(obj, 0) for obj in objectives)
        strictly_better_in_one = any(sol_a.get(obj, 0) > sol_b.get(obj, 0) for obj in objectives)

        return better_in_all and strictly_better_in_one
