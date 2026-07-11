class DeterministicVerifier:
    """
    Verifies that subsequent execution streams output structurally identical byte hashes.
    """
    def __init__(self):
        pass

    def verify_runs_identical(self, list_a: list, list_b: list) -> bool:
        if len(list_a) != len(list_b):
            return False
        for x, y in zip(list_a, list_b):
            if x != y:
                return False
        return True
