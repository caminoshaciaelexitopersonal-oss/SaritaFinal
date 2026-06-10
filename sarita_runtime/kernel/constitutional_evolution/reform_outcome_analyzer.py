class ReformOutcomeAnalyzer:
    """
    Analyzes whether a reform improved or worsened system performance.
    """
    def analyze_outcome(self, reform_id, historical_data):
        # baseline vs post-reform performance comparison
        pre_fitness = historical_data.get("pre_reform_fitness", 0.5)
        post_fitness = historical_data.get("post_reform_fitness", 0.5)

        if post_fitness > pre_fitness + 0.01:
            return "IMPROVED"
        elif post_fitness < pre_fitness - 0.01:
            return "WORSENED"
        else:
            return "STABLE"
