class DominantFutureSelector:
    """
    Selects the dominant future after multiple rounds of competition.
    """
    def select_dominant(self, finalists: list):
        if not finalists:
            return None
        return max(finalists, key=lambda x: x["survival_index"])
