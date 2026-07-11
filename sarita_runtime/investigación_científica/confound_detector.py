class ConfoundDetector:
    """
    Detects unobserved or observed confounding parameters by matching treatment/control groups.
    """
    def __init__(self, graph_builder):
        self.graph_builder = graph_builder

    def find_all_confounders(self, x: str, y: str) -> dict:
        confounders = self.graph_builder.detect_confounders(x, y)
        return {
            "independent": x,
            "dependent": y,
            "observed_confounders": confounders,
            "requires_backdoor_adjustment": len(confounders) > 0
        }
