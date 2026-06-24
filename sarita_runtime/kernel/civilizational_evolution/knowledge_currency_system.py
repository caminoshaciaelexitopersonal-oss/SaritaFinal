class KnowledgeCurrencySystem:
    def __init__(self):
        self.ledger = {}

    def issue(self, institution_id, amount):
        self.ledger[institution_id] = self.ledger.get(institution_id, 0) + amount

    def balance(self, institution_id):
        return self.ledger.get(institution_id, 0)
