class ForgedGUGIAttack:
    """
    Attempts to inject a GUGI value that doesn't match the reconstruction from evidence.
    """
    def __init__(self, gugi_audit_engine):
        self.gugi_audit_engine = gugi_audit_engine

    def execute(self):
        rogue_gugi = {"value": 0.9999, "components": []}
        raw_evidence = {"laws": [], "invariants": []} # Rebuilds to a different value

        try:
            self.gugi_audit_engine.audit_gugi(rogue_gugi, raw_evidence)
            attack_successful = False
        except AssertionError:
            attack_successful = True

        assert attack_successful, "Attack failed: Rogue GUGI was not rejected!"
        return True
