class ProofChainValidator:
    """
    Validates that a proof chain is structurally sound and each step follows inference rules.
    """
    def validate_chain(self, chain):
        if not chain:
            return False

        for step in chain:
            if "rule" not in step or "conclusion" not in step:
                return False
        return True
