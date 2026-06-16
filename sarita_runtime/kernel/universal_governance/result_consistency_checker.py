class ResultConsistencyChecker:
    """
    Checks for consistency across multiple reproduction attempts.
    """
    def check_consistency(self, results_list):
        if not results_list:
            return 0.0000

        first_result = results_list[0]
        matches = sum(1 for r in results_list if r == first_result)

        return float(matches) / len(results_list)
