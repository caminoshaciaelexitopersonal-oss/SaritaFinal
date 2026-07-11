class BenchmarkRunner:
    """
    Sequentially executes cataloged benchmark scenarios and records raw scores.
    """
    def __init__(self):
        pass

    def run_benchmark(self, action_callable, iterations: int = 10) -> list:
        scores = []
        for i in range(iterations):
            score = action_callable(i)
            scores.append(float(score))
        return scores
