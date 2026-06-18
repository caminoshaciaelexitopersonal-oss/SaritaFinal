import time
from sarita_runtime.kernel.epistemic_self_correction.confidence_recalibration_engine import ConfidenceRecalibrationEngine

def run_demo():
    engine = ConfidenceRecalibrationEngine()
    ctx = "AXIOMATIC_PURPOSE"
    initial_conf = 0.95
    timestamp = time.time() - 36000 # 10 hours ago

    print(f"Initial Confidence: {initial_conf}")
    new_conf, trusted = engine.recalibrate(ctx, initial_conf, timestamp, anomalies=2)

    print(f"Recalibrated Confidence (after 10h + 2 anomalies): {new_conf:.4f}")
    print(f"Trusted Status: {trusted}")

if __name__ == "__main__":
    run_demo()
