class ConstitutionalScienceAuditor:
    def audit_science(self, operations):
        # Audits if scientific operations follow the scientific constitution
        for op in operations:
            if op.get("violated_rule"):
                return False
        return True
