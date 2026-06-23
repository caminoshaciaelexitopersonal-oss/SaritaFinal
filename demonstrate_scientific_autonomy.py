from sarita_runtime.kernel.scientific_autonomy.scientific_autonomy_engine import ScientificAutonomyEngine

def run_demo():
    engine = ScientificAutonomyEngine()
    discovery_record = {
        "theory": {"id": "T-RECURSIVE-SOVEREIGNTY"},
        "experiment": {"protocol": "RECURSIVE_STRESS_TEST"}
    }

    print("Certifying scientific autonomy for discovery...")
    cert = engine.certify_autonomy(discovery_record)

    print(f"Valid Discovery: {cert['valid']}")
    print(f"Independent Reasoning: {cert['independent']}")
    print(f"Sovereign Certification Status: {cert['certification']['status']}")

if __name__ == "__main__":
    run_demo()
