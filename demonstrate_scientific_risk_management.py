from sarita_runtime.kernel.scientific_governance.scientific_risk_engine import ScientificRiskEngine

def run_demo():
    engine = ScientificRiskEngine()
    paradigms = [{"unverified_assumptions_count": 5}] # Risk 0.5
    theories = [{"evidence_sources_count": 1}] # Fragility 1.0

    print("Evaluating scientific risk and fragility...")
    risk = engine.evaluate_risk(paradigms, theories, [])

    print(f"Max System Risk: {risk['max_risk']}")
    print(f"Governance Intervention: {risk['intervention']}")

if __name__ == "__main__":
    run_demo()
