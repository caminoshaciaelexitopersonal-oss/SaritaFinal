from sarita_runtime.kernel.recursive_epistemology.recursive_confidence_engine import RecursiveConfidenceEngine

def run_demo():
    engine = RecursiveConfidenceEngine()
    conf = 0.9
    sigma = 0.02
    evidence = {"consistency": 0.88, "variance": 0.025}

    print(f"Calculating recursive confidence for Confidence={conf}, Sigma={sigma}...")
    metrics = engine.get_recursive_metrics(conf, sigma, evidence)

    print(f"Meta-Confidence: {metrics['meta_confidence']:.4f}")
    print(f"Meta-Uncertainty: {metrics['meta_uncertainty']:.4f}")

if __name__ == "__main__":
    run_demo()
