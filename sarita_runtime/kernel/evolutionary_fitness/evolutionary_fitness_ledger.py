import time

class EvolutionaryFitnessLedger:
    """
    Records the evolution of SARITA's constitutional fitness.
    """
    def __init__(self):
        self.entries = []

    def record_fitness(self, fitness: float):
        self.entries.append({"fitness": fitness, "time": time.time()})
        print(f"FITNESS LEDGER: Recorded fitness: {fitness}")
