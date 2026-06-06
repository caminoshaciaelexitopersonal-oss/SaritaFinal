class ConsensusOfConsensusValidator:
    """
    Validates that consensuses being aggregated are truly independent.
    """
    @staticmethod
    def validate_independence(consensuses: list, lineage_tracker):
        # consensuses: list of lists of verifier_ids
        # Check if any verifier in one consensus is related to a verifier in another
        for i, group1 in enumerate(consensuses):
            for group2 in consensuses[i+1:]:
                for v1 in group1:
                    for v2 in group2:
                        if lineage_tracker.are_related(v1, v2):
                            return False, f"Related verifiers {v1} and {v2} found in distinct consensuses."
        return True, "Consensus independence confirmed."
