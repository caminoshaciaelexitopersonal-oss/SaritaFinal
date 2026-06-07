class VerificationOriginValidator:
    """
    Validates the independence of verifier origins.
    """
    @staticmethod
    def validate_independence_of_origin(provenance1: dict, provenance2: dict):
        # Origins must be distinct
        if provenance1["origin"] == provenance2["origin"]:
            return False, "Verifiers share the same origin."

        # Authors must be distinct
        if provenance1["author"] == provenance2["author"]:
            return False, "Verifiers share the same author."

        # Implementation families must be distinct
        if provenance1["implementation"] == provenance2["implementation"]:
            return False, "Verifiers share the same implementation family."

        return True, "Verifier independence of origin confirmed."
