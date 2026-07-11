import itertools

class FactorialDesignEngine:
    """
    Constructs full-factorial, fractional-factorial, or response surface design arrays for multiple variables.
    """
    def __init__(self):
        pass

    def build_full_factorial(self, factors: dict) -> list:
        keys = list(factors.keys())
        values = list(factors.values())
        combinations = list(itertools.product(*values))

        runs = []
        for combo in combinations:
            run_dict = {}
            for i, key in enumerate(keys):
                run_dict[key] = combo[i]
            runs.append(run_dict)
        return runs
