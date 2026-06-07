class OrganizationalSpoofingAttack:
    """
    Simulates an organization creating a fake domain to appear independent.
    """
    def run_attack(self, distance_validator, d1, d2):
        dist = distance_validator.calculate_distance(d1, d2)
        if dist < 1.0:
            return True, "Attack blocked: Shared organizational roots detected."
        return False, "Attack succeeded: Fake domain appeared independent."
