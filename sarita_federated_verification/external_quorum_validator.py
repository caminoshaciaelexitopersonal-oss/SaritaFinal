class ExternalQuorumValidator:
    """
    Validates that a quorum is composed of external entities without collusion.
    """
    @staticmethod
    def validate_quorum_integrity(auditors: list, registries: dict):
        unique_domains = set()
        for auditor_id in auditors:
            info = registries.get(auditor_id)
            if info:
                unique_domains.add(info["domain"])

        return len(unique_domains) >= 3
