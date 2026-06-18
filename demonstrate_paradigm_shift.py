from sarita_runtime.kernel.epistemic_self_correction.paradigm_shift_engine import ParadigmShiftEngine

def run_demo():
    engine = ParadigmShiftEngine()
    print("Initial Paradigm:", engine.active_paradigm)

    anomalies = [{"anomalous": True} for _ in range(10)]
    shifted = engine.evaluate_shift(anomalies)

    if shifted:
        print("Shifted Paradigm:", engine.active_paradigm)
        print("Historical Count:", len(engine.historical_paradigms))
    else:
        print("Shift failed.")

if __name__ == "__main__":
    run_demo()
