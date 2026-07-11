from .hypothesis_engine import ScientificHypothesis

class HypothesisRegistry:
    """
    Maintains a record and lookup mechanism for all scientific hypotheses.
    """
    def __init__(self):
        self.hypotheses = {}

    def register(self, hypothesis: ScientificHypothesis):
        self.hypotheses[hypothesis.hypothesis_id] = hypothesis

    def get(self, hypothesis_id: str) -> ScientificHypothesis:
        return self.hypotheses.get(hypothesis_id)

    def list_all(self) -> list:
        return list(self.hypotheses.values())

    def clear(self):
        self.hypotheses.clear()
