class StrategicConflictResolver:
    """
    Resolves conflicts between high-level strategic domains (Security vs Autonomy).
    """
    def resolve_conflict(self, domain_a: str, domain_b: str, context: dict):
        # In SARITA, Sovereignty and Autonomy usually take precedence.
        if domain_a == "AUTONOMY" or domain_b == "AUTONOMY":
            return "AUTONOMY"
        return domain_a
