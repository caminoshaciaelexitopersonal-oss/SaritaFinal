import hashlib
import json
import logging

class ForensicHashEngine:
    @staticmethod
    def calculate_sha256(payload, previous_hash, trace_id):
        # 48.2 - Criptográficamente real
        data_to_hash = {
            "payload_hash": hashlib.sha256(json.dumps(payload).encode()).hexdigest(),
            "previous_hash": previous_hash,
            "trace_id": trace_id
        }
        hash_string = json.dumps(data_to_hash, sort_keys=True)
        return hashlib.sha256(hash_string.encode()).hexdigest()

    def validate_chain(self, current_record, previous_record):
        expected_hash = self.calculate_sha256(
            current_record['payload'],
            previous_record['integrity_hash'],
            current_record['trace_id']
        )
        return current_record['integrity_hash'] == expected_hash

if __name__ == "__main__":
    engine = ForensicHashEngine()
    h = engine.calculate_sha256({"amount": 100}, "initial-hash", "trace-123")
    print(f"Generated Forensic Hash: {h}")
