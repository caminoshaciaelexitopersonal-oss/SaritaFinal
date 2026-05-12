import hashlib
import json

class StateReplication:
    def __init__(self):
        self.snapshots = {}

    def create_snapshot(self, domain, state_data):
        checksum = hashlib.sha256(json.dumps(state_data).encode()).hexdigest()
        snapshot = {
            "domain": domain,
            "data": state_data,
            "checksum": checksum,
            "version": len(self.snapshots.get(domain, [])) + 1
        }
        if domain not in self.snapshots:
            self.snapshots[domain] = []
        self.snapshots[domain].append(snapshot)
        print(f"Snapshot created for {domain} version {snapshot['version']}")
        return snapshot

    def validate_replication(self, domain, version, target_checksum):
        # Checks if replica matches master checksum
        snapshot = self.snapshots[domain][version-1]
        return snapshot['checksum'] == target_checksum

if __name__ == "__main__":
    sr = StateReplication()
    sr.create_snapshot("FINANCE", {"balance": 1000})
