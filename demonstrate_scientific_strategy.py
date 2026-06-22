from sarita_runtime.kernel.scientific_governance.scientific_strategy_engine import ScientificStrategyEngine

def run_demo():
    engine = ScientificStrategyEngine()
    domain_stats = {
        "AXIOMATIC_REASONING": {"gap_severity": 0.8, "value_estimate": 0.95},
        "RECURSIVE_DYNAMICS": {"gap_severity": 0.4, "value_estimate": 0.8},
        "HISTORICAL_DATA": {"gap_severity": 0.2, "value_estimate": 0.1}
    }

    print("Developing sovereign scientific strategy...")
    strategy = engine.develop_strategy(domain_stats)

    print("Priorities:", strategy["priorities"])
    print("Strategic Roadmap:", strategy["roadmap"])
    print(f"Strategic Alignment Score: {strategy['strategic_alignment']}")

if __name__ == "__main__":
    run_demo()
