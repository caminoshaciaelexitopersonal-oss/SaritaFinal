from sarita_runtime.kernel.civilizational_emergence.civilization_history_engine import CivilizationHistoryEngine

def run_demo():
    engine = CivilizationHistoryEngine()
    print("Recording civilizational events...")
    engine.record_civilization_event("FOUNDING_OF_INSTITUTIONS")
    engine.record_civilization_event("SCIENTIFIC_REVOLUTION")

    audit = engine.audit_history()
    print(f"Historical Audit: {audit}")

if __name__ == "__main__":
    run_demo()
