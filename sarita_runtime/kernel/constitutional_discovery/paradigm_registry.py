class ParadigmRegistry:
    """
    Registry for all discovered governance paradigms.
    """
    def __init__(self, ledger):
        self.paradigms = {}
        self.ledger = ledger

    def register(self, paradigm):
        self.paradigms[paradigm["paradigm_id"]] = paradigm
        self.ledger.record_paradigm(paradigm)
