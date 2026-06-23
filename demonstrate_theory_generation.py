from sarita_runtime.kernel.scientific_autonomy.scientific_discovery_engine import ScientificDiscoveryEngine

def run_demo():
    engine = ScientificDiscoveryEngine()
    domain_data = {"domain_id": "RECURSION_LOGIC"}

    print("Performing autonomous scientific discovery...")
    discovery = engine.perform_discovery(domain_data)

    print("New Hypothesis Generated:", discovery["hypothesis"]["statement"])
    print("Theory Synthesized ID:", discovery["theory"]["id"])
    print("Experimental Protocol:", discovery["experiment"]["protocol"])
    print("Refined Theory Evidence Score:", discovery["theory"]["evidence_score"])

if __name__ == "__main__":
    run_demo()
