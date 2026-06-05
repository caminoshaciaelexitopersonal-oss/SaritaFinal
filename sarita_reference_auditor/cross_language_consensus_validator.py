class CrossLanguageConsensusValidator:
    """
    Validates that verifiers written in different languages reach the same consensus.
    """
    def __init__(self):
        self.language_results = {} # package_hash -> {lang: result}

    def register_result(self, package_hash: str, lang: str, result: bool):
        if package_hash not in self.language_results:
            self.language_results[package_hash] = {}
        self.language_results[package_hash][lang] = result

    def verify_multi_language_consensus(self, package_hash: str):
        results = self.language_results.get(package_hash, {})
        if len(results) < 2:
            return False, "Insufficient language diversity for consensus."

        verdict_values = list(results.values())
        if all(v == verdict_values[0] for v in verdict_values):
            return True, "Multi-language consensus achieved."
        return False, "Divergence detected between language implementations!"
