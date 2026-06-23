from sarita_runtime.kernel.scientific_civilization.cognitive_civilization_engine import CognitiveCivilizationEngine

def run_demo():
    engine = CognitiveCivilizationEngine()
    civs = [
        {"id": "CIV-A", "coherence": 0.95},
        {"id": "CIV-B", "coherence": 0.88}
    ]

    print(f"Simulating cognitive civilization ecosystem ({len(civs)} active civilizations)...")
    sim = engine.run_civilization_simulation(civs)

    print("Top Fitness Civilization:", sim["top_fitness"])
    print("Ecosystem Stats:", sim["ecosystem_stats"])

if __name__ == "__main__":
    run_demo()
