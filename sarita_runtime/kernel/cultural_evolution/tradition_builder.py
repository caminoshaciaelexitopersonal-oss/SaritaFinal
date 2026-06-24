import hashlib

class TraditionBuilder:
    def __init__(self):
        self.traditions = {}

    def build_tradition(self, civ_id, cultural_state):
        state_str = str(sorted(cultural_state.items()))
        tradition_hash = hashlib.sha256(f"{civ_id}:{state_str}".encode()).hexdigest()[:12]

        tradition = {
            "id": tradition_hash,
            "civ_id": civ_id,
            "content": cultural_state,
            "resilience": cultural_state.get("ritualistic", 0.5)
        }
        self.traditions[tradition_hash] = tradition
        return tradition
