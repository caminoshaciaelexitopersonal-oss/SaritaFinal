class OrganizationalDistanceValidator:
    """
    Measures the organizational distance between two entities.
    """
    @staticmethod
    def calculate_distance(domain1: str, domain2: str):
        # Very simple simulation: common TLD or same domain name
        if domain1 == domain2: return 0.0

        parts1 = domain1.split('.')
        parts2 = domain2.split('.')

        if parts1[-2:] == parts2[-2:]:
            return 0.5 # Shared parent organization

        return 1.0 # Completely distinct
