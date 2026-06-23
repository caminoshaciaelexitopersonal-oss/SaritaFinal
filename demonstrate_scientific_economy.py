from sarita_runtime.kernel.scientific_civilization.scientific_economy_engine import ScientificEconomyEngine

def run_demo():
    engine = ScientificEconomyEngine()
    data = {
        "unit": {"utility": 0.8, "novelty": 0.9},
        "path": ["S1", "S2", "S3"]
    }

    print("Auditing scientific economy...")
    audit = engine.audit_economy(data)

    print(f"Knowledge Value: {audit['value']:.2f}")
    print(f"Cognitive Cost: {audit['cost']:.2f}")
    print(f"Research ROI: {audit['roi']:.2f}")

if __name__ == "__main__":
    run_demo()
