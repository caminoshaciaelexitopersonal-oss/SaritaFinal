from sarita_runtime.kernel.scientific_civilization.knowledge_sustainability_engine import KnowledgeSustainabilityEngine

def run_demo():
    engine = KnowledgeSustainabilityEngine()
    landscape = {"fragmentation": 0.2, "inconsistency": 0.1}
    metrics = {"access": 0.9, "update": 0.8}

    print("Auditing knowledge sustainability...")
    audit = engine.audit_sustainability(landscape, metrics)

    print(f"Stability Index: {audit['stability']:.4f}")
    print(f"Resilience Actions: {audit['resilience_actions']}")

if __name__ == "__main__":
    run_demo()
