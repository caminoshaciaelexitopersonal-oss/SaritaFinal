class CollectiveProblemSolver:
    def solve_meta_problem(self, difficulty, collective_power):
        success_rate = min(1.0, collective_power / difficulty)
        return success_rate > 0.7
