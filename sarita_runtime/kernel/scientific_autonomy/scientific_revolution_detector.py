class ScientificRevolutionDetector:
    def detect_revolution(self, current_dominant_theory, challenger_theory):
        # Detects a scientific revolution when a challenger significantly outperforms the dominant theory
        if challenger_theory.get("evidence_score", 0) > current_dominant_theory.get("evidence_score", 0) + 0.2:
            return True
        return False
