from sarita_runtime.kernel.scientific_governance.future_frontier_engine import FutureFrontierEngine

def run_demo():
    engine = FutureFrontierEngine()
    current_state = {"density": 0.5}

    print("Discovering future scientific frontiers...")
    frontiers = engine.discover_frontiers(current_state)

    print("New Frontiers Proposed:", frontiers["new_frontiers"])
    print("Top Research Opportunity:", frontiers["top_opportunity"])

if __name__ == "__main__":
    run_demo()
