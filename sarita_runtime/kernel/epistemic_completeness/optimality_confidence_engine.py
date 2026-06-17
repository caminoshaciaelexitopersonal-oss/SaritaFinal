import time

class OptimalityConfidenceEngine:
    """
    Engine to generate Confidence of Global Optimality based on search boundaries.
    """
    def __init__(self, global_estimator, local_analyzer, ledger):
        self.global_estimator = global_estimator
        self.local_analyzer = local_analyzer
        self.ledger = ledger

    def calculate_optimality_confidence(self, selected_arch, search_completeness_res, boundary_res):
        print(f"[OptimalityConfidenceEngine] Calculating global optimality confidence for: {selected_arch.get('id')}...")

        global_est = self.global_estimator.estimate_global_optimality(selected_arch, search_completeness_res)
        local_v_global = self.local_analyzer.analyze_local_vs_global(selected_arch, boundary_res)

        confidence = (global_est * 0.7) + (local_v_global * 0.3)

        result = {
            "global_optimality_confidence": round(confidence, 4),
            "is_global_best_likely": confidence > 0.9,
            "confidence_derivation": "hybrid_epistemic_analysis",
            "timestamp": time.time()
        }

        self.ledger.record_bound(result)
        return result
