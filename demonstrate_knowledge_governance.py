from sarita_runtime.kernel.scientific_governance.knowledge_governance_engine import KnowledgeGovernanceEngine

def run_demo():
    engine = KnowledgeGovernanceEngine()
    pool = {
        "T-01": {"age": 50, "evidence": 0.8},
        "T-OBS": {"age": 1000, "evidence": 0.1, "obsolescence_duration": 600}
    }

    print("Governing knowledge lifecycle...")
    governance = engine.govern_knowledge(pool)

    for t_id, res in governance.items():
        print(f"Theory: {t_id}, State: {res['state']}, Retired: {res['retired']}")

if __name__ == "__main__":
    run_demo()
