import random

class LawSelectionEngine:
    def __init__(self, evaluator):
        self.evaluator = evaluator

    def select_best_laws(self, law_pool, performance_map):
        scored_laws = []
        for laws in law_pool:
            perf = performance_map.get(id(laws), random.uniform(0.1, 0.5))
            fitness = self.evaluator.evaluate_fitness(laws, perf)
            scored_laws.append((laws, fitness))

        scored_laws.sort(key=lambda x: x[1], reverse=True)
        return [laws for laws, score in scored_laws[:len(scored_laws)//2 + 1]]

    def check_extinction(self, laws, fitness):
        return fitness < 0.2
