class ProtocolComparator:
    """
    Compares two protocols to highlight delta shifts in variables or repetitions.
    """
    def __init__(self):
        pass

    def compare(self, p1_dict: dict, p2_dict: dict) -> dict:
        delta = {
            "hypothesis_changed": p1_dict.get("hypothesis") != p2_dict.get("hypothesis"),
            "repetitions_delta": p1_dict.get("repetitions", 0) - p2_dict.get("repetitions", 0)
        }
        return delta
