import os
import ast

class TechnicalDebtEngine:
    """
    Calculates complexity, maintainability, and architectural smells.
    Phase 128.5.
    """
    def __init__(self, model):
        self.model = model

    def calculate_complexity(self, filepath):
        try:
            with open(filepath, "r") as f:
                tree = ast.parse(f.read())
                complexity = 0
                for node in ast.walk(tree):
                    if isinstance(node, (ast.If, ast.For, ast.While, ast.And, ast.Or)):
                        complexity += 1
                return complexity
        except Exception:
            return 0

    def estimate_maintainability(self, filepath):
        # Simplistic Maintainability Index (MI)
        complexity = self.calculate_complexity(filepath)
        size = os.path.getsize(filepath)
        if size == 0: return 1.0
        score = 1.0 - (complexity / 50.0) - (size / 10000.0)
        return max(0.0, min(1.0, score))

    def detect_architectural_smells(self):
        smells = []
        # Smell: God Module (too many files)
        for module, files in self.model.get("modules", {}).items():
            if len(files) > 15:
                smells.append({
                    "type": "GOD_MODULE",
                    "module": module,
                    "count": len(files)
                })
        return smells

    def get_aggregate_metrics(self):
        files = self.model.get("files", [])
        total_complexity = sum(self.calculate_complexity(f) for f in files)
        avg_maintainability = sum(self.estimate_maintainability(f) for f in files) / len(files) if files else 1.0

        return {
            "total_complexity": total_complexity,
            "avg_maintainability": round(avg_maintainability, 4),
            "debt_ratio": round(total_complexity / 1000.0, 4), # Symbolic ratio
            "smells": self.detect_architectural_smells()
        }
