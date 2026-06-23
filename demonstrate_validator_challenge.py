from sarita_runtime.kernel.recursive_epistemology.meta_falsifiability_engine import MetaFalsifiabilityEngine

def run_demo():
    engine = MetaFalsifiabilityEngine()
    indices = {"GMEI": 0.98, "GSCI": 0.99, "GRESI": 0.95}

    print("Stress testing sovereign indices with meta-falsifiability...")
    results = engine.stress_test_indices(indices)

    for idx, res in results.items():
        print(f"Index: {idx}, Refuted: {res['refuted']}, Survival Score: {res['survival_score']:.4f}")

if __name__ == "__main__":
    run_demo()
