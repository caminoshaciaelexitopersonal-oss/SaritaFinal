import hashlib
import time

class SovereignAuditChain:
    def __init__(self):
        self.chain = []

    def append_audit_event(self, actor, action, previous_hash):
        timestamp = time.time()
        payload = f"{actor}:{action}:{timestamp}"
        current_hash = hashlib.sha256((payload + previous_hash).encode()).hexdigest()

        event = {
            "actor": actor,
            "action": action,
            "timestamp": timestamp,
            "prev_hash": previous_hash,
            "hash": current_hash
        }
        self.chain.append(event)
        return current_hash

    def validate_full_chain(self):
        for i in range(1, len(self.chain)):
            if self.chain[i]["prev_hash"] != self.chain[i-1]["hash"]:
                return False, f"Chain broken at index {i}"
        return True, "CHAIN_INTEGRITY_VERIFIED"

if __name__ == "__main__":
    audit = SovereignAuditChain()
    h1 = audit.append_audit_event("AI_GOVERNOR", "QUARANTINE_AGENT", "0"*64)
    h2 = audit.append_audit_event("DEPLOYMENT_GOV", "ROLLING_UPDATE", h1)
    print(audit.validate_full_chain())
