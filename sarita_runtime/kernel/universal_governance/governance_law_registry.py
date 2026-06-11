class GovernanceLawRegistry:
    """
    Registry for discovered and certified governance laws.
    """
    def __init__(self, ledger=None):
        self.laws = {}
        self.ledger = ledger

    def register_law(self, law):
        self.laws[law["law_id"]] = law
        if self.ledger:
            self.ledger.record_law_registration(law)

    def get_law(self, law_id):
        return self.laws.get(law_id)
