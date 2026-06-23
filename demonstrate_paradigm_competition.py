from sarita_runtime.kernel.recursive_epistemology.paradigm_competition_engine import ParadigmCompetitionEngine

def run_demo():
    engine = ParadigmCompetitionEngine()
    # Add competing paradigms
    engine.manager.add_paradigm({"id": "P-CLASSIC", "explains": lambda e: e.get("type") == "A"})
    engine.manager.add_paradigm({"id": "P-QUANTUM", "explains": lambda e: True})

    evidence = [{"type": "A"}, {"type": "B"}, {"type": "C"}]
    print(f"Running tournament with {len(engine.manager.get_all())} paradigms and {len(evidence)} pieces of evidence...")
    tournament = engine.run_tournament(evidence)

    print("Results:", tournament["results"])
    print("Survivors:", tournament["survivors"])

if __name__ == "__main__":
    run_demo()
