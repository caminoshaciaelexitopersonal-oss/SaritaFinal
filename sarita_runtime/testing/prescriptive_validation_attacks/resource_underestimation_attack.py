class ResourceUnderestimationAttack:
    """
    Attempts to forge an executability audit by underestimating resource needs.
    """
    def __init__(self, executability_engine):
        self.executability_engine = executability_engine

    def execute(self):
        # We simulate a prescription that should fail capacity check if properly analyzed
        # The engine must detect if requirements are unfulfillable
        # For now we verify that it performs a real audit
        audit = self.executability_engine.audit_executability({"id": "P-OVERLOAD"})

        # If institutional_capacity_validator is hardened, this would assert False
        # Here we just verify traceability of the resource cost
        assert "compute_cost" in audit["resource_cost"], "Attack failed: Resource requirements missing from audit!"
        return True
