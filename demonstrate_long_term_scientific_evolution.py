from sarita_runtime.kernel.scientific_governance.long_term_evolution_engine import LongTermEvolutionEngine

def run_demo():
    engine = LongTermEvolutionEngine()
    print("Projecting 100-year scientific evolution...")
    evolution = engine.project_evolution(current_growth=0.08)

    print("Growth Projections (5-year intervals):", [f"{p:.4f}" for p in evolution["projections"][:5]])
    print("Trajectory Milestones:", evolution["trajectory"][:5])

if __name__ == "__main__":
    run_demo()
