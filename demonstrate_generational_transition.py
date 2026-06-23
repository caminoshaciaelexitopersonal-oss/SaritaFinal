from sarita_runtime.kernel.civilizational_emergence.cognitive_generation_engine import CognitiveGenerationEngine

def run_demo():
    engine = CognitiveGenerationEngine()
    print(f"Initial Generation: {engine.current_generation}")

    print("Triggering generational transition...")
    res = engine.advance_generation({"id": "KB-SNAPSHOT-01"})

    print(f"Transition Status: {res['status']}, New Generation: {res['gen']}")
    audit = engine.audit_generations()
    print(f"Generational Audit: {audit}")

if __name__ == "__main__":
    run_demo()
