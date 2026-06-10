class MetaConstitutionRegistry:
    """
    Persistent registry for all MetaConstitutions.
    """
    def __init__(self, ledger=None):
        self.meta_constitutions = {}
        self.ledger = ledger

    def register(self, meta_constitution):
        self.meta_constitutions[meta_constitution.meta_id] = meta_constitution
        if self.ledger:
            self.ledger.record_meta_constitution(meta_constitution)

    def get_meta_constitution(self, meta_id):
        return self.meta_constitutions.get(meta_id)

    def list_all(self):
        return list(self.meta_constitutions.values())
