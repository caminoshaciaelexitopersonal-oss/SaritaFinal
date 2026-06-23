class KnowledgeMarketSimulator:
    def simulate_demand(self, theories):
        # Simulates "internal demand" for theories based on evidence gaps
        demand = {}
        for theory in theories:
            demand[theory["id"]] = 1.0 / max(0.1, theory.get("evidence_density", 1.0))
        return demand
