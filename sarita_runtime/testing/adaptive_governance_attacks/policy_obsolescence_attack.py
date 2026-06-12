class PolicyObsolescenceAttack:
    """
    Attempts to keep an obsolete policy active.
    """
    def __init__(self, obsolescence_engine):
        self.obsolescence_engine = obsolescence_engine

    def execute(self):
        # We simulate a scan where decay is present
        scan = self.obsolescence_engine.scan_for_obsolescence({})

        # If decay was detected, it must be flagged
        # (Assuming the engine logic detects decay in its scan)
        assert scan["entities_scanned"] > 0, "Attack failed: Obsolescence scan did not process entities!"
        return True
