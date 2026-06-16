class NonUniversalInvariantAttack:
    """
    Attempts to certify an invariant that does not meet the universality threshold.
    """
    def __init__(self, revalidation_engine):
        self.revalidation_engine = revalidation_engine

    def execute(self):
        class WeakInvariant:
            id = "INV-WEAK-001"
            def check(self, universe):
                return False # Always fails

        # The revalidation must fail and raise AssertionError
        try:
            self.revalidation_engine.revalidate_invariants([WeakInvariant()])
            attack_successful = False
        except AssertionError:
            attack_successful = True

        assert attack_successful, "Attack failed: Weak invariant was not rejected!"
        return True
