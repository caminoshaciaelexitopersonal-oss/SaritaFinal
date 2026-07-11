class ProtocolRegistry:
    """
    Registry containing standard operating protocol parameters.
    """
    def __init__(self):
        self._protocols = {}

    def register_protocol(self, proto_id: str, details: dict):
        self._protocols[proto_id] = details

    def get_protocol(self, proto_id: str) -> dict:
        return self._protocols.get(proto_id, {})
