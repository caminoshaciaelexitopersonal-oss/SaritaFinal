class UnverifiableLawReportAttack:
    """
    Attempts to register a law that has no verifiable scientific origin.
    """
    def __init__(self, traceability_engine):
        self.traceability_engine = traceability_engine

    def execute(self):
        # A law without origin data
        rogue_law_id = "LAW-ROGUE-001"

        # The audit must reject it
        audit_result = self.traceability_engine.audit_entity(rogue_law_id)

        assert audit_result["status"] == "REJECTED", "Attack failed: Rogue law was not rejected!"
        return True
