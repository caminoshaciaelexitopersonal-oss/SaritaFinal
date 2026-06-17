import hashlib

class CapabilityNoveltyDetector:
    """
    Distinguishes between Adaptation, Optimization, Reconfiguration, Selection, and Meta-evolution.
    """
    def detect_evolution_category(self, capability_data, history):
        # 1. Structural Hash Comparison (Detects Reconfiguration/Selection)
        struct_hash = hashlib.sha256(str(capability_data.get("structure")).encode()).hexdigest()
        is_known_template = struct_hash in history.get("known_templates", [])

        # 2. Performance Delta (Detects Optimization/Adaptation)
        perf_delta = capability_data.get("performance_gain", 0.0)
        is_linear_gain = 0.0 < perf_delta < 0.15

        # 3. Axiomatic Derivation Check (Detects Meta-evolution)
        axiom_link = capability_data.get("axiom_derivation_proof")
        is_derived = axiom_link is not None and axiom_link in history.get("certified_axioms", [])

        # Categorization Logic
        if is_derived and not is_known_template and perf_delta > 0.2:
            return "META_EVOLUTION_AUTHENTIC"
        elif is_known_template and is_linear_gain:
            return "RECONFIGURATION_TEMPLATE"
        elif not is_known_template and is_linear_gain:
            return "ADAPTATION_ENVIRONMENTAL"
        elif is_known_template and perf_delta > 0.1:
            return "OPTIMIZATION_PARAMETRIC"
        elif is_known_template:
            return "SELECTION_STATIC"
        else:
            return "UNKNOWN_STRUCTURAL_SHIFT"

    def calculate_originality_index(self, category):
        weights = {
            "META_EVOLUTION_AUTHENTIC": 1.0,
            "ADAPTATION_ENVIRONMENTAL": 0.7,
            "OPTIMIZATION_PARAMETRIC": 0.5,
            "RECONFIGURATION_TEMPLATE": 0.3,
            "SELECTION_STATIC": 0.1,
            "UNKNOWN_STRUCTURAL_SHIFT": 0.0
        }
        return weights.get(category, 0.0)
