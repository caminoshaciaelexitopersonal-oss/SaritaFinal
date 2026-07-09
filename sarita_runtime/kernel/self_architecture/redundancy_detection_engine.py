import os
import hashlib

class RedundancyDetectionEngine:
    """
    Detects duplicated logic, engines, and dead features.
    Phase 128.4.
    """
    def __init__(self, model):
        self.model = model
        self.redundancies = []

    def detect_engine_duplication(self):
        engines = [m for m in self.model.get("modules", {}) if "engine" in m.lower()]
        # Check for similar names or overlapping files
        for i in range(len(engines)):
            for j in range(i + 1, len(engines)):
                if engines[i][:5] == engines[j][:5]:
                    self.redundancies.append({
                        "type": "ENGINE_DUPLICATION",
                        "items": [engines[i], engines[j]],
                        "confidence": 0.75
                    })
        return self.redundancies

    def detect_similar_algorithms(self):
        # Implementation would use content hashing or AST comparison
        # For now, placeholder based on file naming patterns
        files = self.model.get("files", [])
        for i in range(len(files)):
            for j in range(i + 1, len(files)):
                if os.path.basename(files[i]) == os.path.basename(files[j]):
                    self.redundancies.append({
                        "type": "FILE_OVERLAP",
                        "items": [files[i], files[j]],
                        "confidence": 0.99
                    })
        return self.redundancies

    def detect_dead_features(self):
        # Check for files that are not imported by anyone in the graph
        # For now, return a placeholder based on 'test' or 'unused' naming
        dead = [f for f in self.model.get("files", []) if "unused" in f.lower()]
        return [{"type": "DEAD_CODE", "path": f} for f in dead]

    def generate_report(self):
        return {
            "redundancies": self.redundancies,
            "dead_features": self.detect_dead_features()
        }
