from sarita_runtime.kernel.scientific_civilization.civilization_continuity_engine import CivilizationContinuityEngine

def run_demo():
    engine = CivilizationContinuityEngine()
    vault = {"state": "SNAPSHOT"}
    archive = {"integrity_check": True}

    print("Certifying civilizational continuity after simulated reset...")
    cert = engine.certify_civilization_survival(vault, archive)

    print(f"Recovered: {cert['recovered']}")
    print(f"Continuity Certified: {cert['continuity_certified']}")

if __name__ == "__main__":
    run_demo()
