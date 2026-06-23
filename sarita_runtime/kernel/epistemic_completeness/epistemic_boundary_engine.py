import time

class EpistemicBoundaryEngine:
    """
    Engine to identify what the system knows, what it doesn't, and what it couldn't explore.
    """
    def __init__(self, limit_detector, unknown_estimator, surface_builder, ledger):
        self.limit_detector = limit_detector
        self.unknown_estimator = unknown_estimator
        self.surface_builder = surface_builder
        self.ledger = ledger

    def certify_epistemic_boundaries(self, search_completeness_res):
        print("[EpistemicBoundaryEngine] Mapping uncertainty surface and knowledge limits...")

        limits = self.limit_detector.detect_knowledge_limits()
        unknowns = self.unknown_estimator.estimate_unknown_unknowns(search_completeness_res)
        surface = self.surface_builder.build_uncertainty_surface(limits, unknowns)

        result = {
            "knowledge_limit_depth": round(sum(limits.values()) / len(limits), 4) if limits else 0.0,
            "uncertainty_index": round(unknowns["factor"], 4),
            "boundary_awareness_certified": True,
            "timestamp": time.time()
        }

        self.ledger.record_bound(result)
        return result
