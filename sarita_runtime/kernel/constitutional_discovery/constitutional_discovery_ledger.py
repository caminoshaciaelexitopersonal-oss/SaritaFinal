import time

class ConstitutionalDiscoveryLedger:
    """
    Ledger for recording constitutional discoveries.
    """
    def __init__(self, name="DiscoveryLedger"):
        self.name = name
        self.entries = []

    def record(self, event_type, data):
        entry = {
            "timestamp": time.time(),
            "event_type": event_type,
            "data": data
        }
        self.entries.append(entry)
        return entry

    def record_discovery(self, config, novelty):
        self.record("CONSTITUTIONAL_DISCOVERY", {"config_id": config["id"], "novelty": novelty})

    def record_rejection(self, attack_name, reason):
        self.record("REJECTION", {"attack": attack_name, "reason": reason})

class AxiomDiscoveryLedger(ConstitutionalDiscoveryLedger):
    def record_axiom_discovery(self, axiom):
        self.record("AXIOM_DISCOVERED", axiom)

class ParadigmDiscoveryLedger(ConstitutionalDiscoveryLedger):
    def record_paradigm(self, paradigm):
        self.record("PARADIGM_DISCOVERED", paradigm)

class CivilizationalInventionLedger(ConstitutionalDiscoveryLedger):
    def record_civilization_design(self, design):
        self.record("CIVILIZATION_INVENTED", design)
