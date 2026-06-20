from sarita_runtime.kernel.scientific_autonomy.theory_competition_engine import TheoryCompetitionEngine

def run_demo():
    engine = TheoryCompetitionEngine()
    theories = [
        {"id": "T-01", "evidence_score": 0.85},
        {"id": "T-02", "evidence_score": 0.92},
        {"id": "T-03", "evidence_score": 0.70}
    ]

    print(f"Running theory tournament for {len(theories)} theories...")
    competition = engine.run_competition(theories, [])

    print("Rankings:", competition["rankings"])
    print("Survivors:", competition["survivors"])
    print("Scientific Revolution Detected:", competition["revolution_detected"])

if __name__ == "__main__":
    run_demo()
