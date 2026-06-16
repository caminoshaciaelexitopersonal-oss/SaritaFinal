import time

class EvolutionSimulationEngine:
    """
    Engine to simulate 10,000 lines over 1,000 generations.
    """
    def __init__(self, future_gen, gen_evaluator, outcome_predictor, ledger):
        self.future_gen = future_gen
        self.gen_evaluator = gen_evaluator
        self.outcome_predictor = outcome_predictor
        self.ledger = ledger

    def simulate_evolution(self, lines=10000, generations=1000):
        print(f"[EvolutionSimulationEngine] Simulating {lines} lines over {generations} generations...")

        start_time = time.time()
        simulation_data = []

        for line_id in range(lines):
            line_result = self._simulate_line(line_id, generations)
            simulation_data.append(line_result)

            if line_id % 2500 == 0:
                print(f"Simulated {line_id} lines...")

        prediction = self.outcome_predictor.predict_long_term_outcome(simulation_data)

        result = {
            "lines_simulated": lines,
            "generations_per_line": generations,
            "simulation_time": time.time() - start_time,
            "consensus_outcome": prediction
        }

        self.ledger.record_event("EVOLUTION_SIMULATION", result)
        return result

    def _simulate_line(self, line_id, generations):
        current_state = {"fitness": 0.5, "gen": 0}
        for gen in range(generations):
            next_state = self.future_gen.generate_next_generation(current_state)
            eval_res = self.gen_evaluator.evaluate_generation(next_state)
            current_state = next_state
            current_state["fitness"] = eval_res["fitness"]
        return current_state
