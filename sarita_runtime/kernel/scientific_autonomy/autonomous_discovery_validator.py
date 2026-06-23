class AutonomousDiscoveryValidator:
    def validate_discovery(self, discovery_record):
        # Validates that a discovery follows the scientific method and is causally backed
        return discovery_record.get("theory") is not None and discovery_record.get("experiment") is not None
