class GovernanceMetricRebuilder:
    """
    Rebuilds governance metrics from raw scientific evidence.
    """
    def rebuild_metric(self, raw_data):
        """
        Reconstructs the governance metric by weighting laws and invariants.
        """
        laws = raw_data.get("laws", [])
        invariants = raw_data.get("invariants", [])

        laws_weight = sum(l.get("confidence", 0) for l in laws)
        invariants_weight = sum(i.get("universality", 0) for i in invariants)

        total_count = len(laws) + len(invariants)
        if total_count == 0:
            return 0.0000

        return (laws_weight + invariants_weight) / total_count
