class CommonOriginAttack:
    """
    Simulates multiple verifiers that appear independent but share the same origin.
    The Meta-Verification layer should detect the shared origin.
    """
    def run_attack(self, registry, validator):
        v1 = {"origin": "org_A", "author": "Alice", "domain": "a.com", "implementation": "v1", "language": "Python"}
        v2 = {"origin": "org_A", "author": "Bob", "domain": "b.com", "implementation": "v2", "language": "Go"}

        success, msg = validator.validate_independence_of_origin(v1, v2)
        if not success and "origin" in msg:
            return True, "Attack blocked: Common origin detected."
        return False, "Attack succeeded: Common origin was not detected."
