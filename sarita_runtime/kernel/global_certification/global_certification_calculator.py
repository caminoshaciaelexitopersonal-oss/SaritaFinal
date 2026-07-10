class GlobalCertificationCalculator:
    """
    Calculates the Global Global Certification Index (GGCI).
    Phase 129.14.
    """
    def calculate_ggci(self, certification_results):
        if not certification_results: return 0.0

        scores = [res["score"] for res in certification_results.values()]
        ggci = sum(scores) / len(scores)
        return round(ggci, 4)

class GlobalGlobalCertificationIndex:
    def __init__(self):
        self.calculator = GlobalCertificationCalculator()
        self.latest_ggci = 0.0

    def update_index(self, results):
        self.latest_ggci = self.calculator.calculate_ggci(results)
        return self.latest_ggci
