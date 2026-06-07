class EvidenceSubstitutionAttack:
    """
    Attempts to substitute a valid SUEP package with a modified one.
    """
    def run_attack(self, validator, original_package):
        corrupt_package = original_package.copy()
        corrupt_package["payload"]["initial_state"]["corrupted"] = True
        # The validator should detect that the package hash no longer matches or the signatures are invalid.
        pass
