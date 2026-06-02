import logging

class CausalReplayValidator:
    """
    Validates that a replayed graph matches the original intent.
    """
    @staticmethod
    def validate_consistency(original_graph, replayed_graph):
        logging.info("Validator: Verifying replayed state consistency.")

        # Compare Ownership
        if original_graph.ownership != replayed_graph.ownership:
            return False, "Ownership mismatch"

        # Compare Pressure
        if original_graph.global_pressure != replayed_graph.global_pressure:
            return False, "Pressure mismatch"

        # Compare Epoch
        if original_graph.active_epoch != replayed_graph.active_epoch:
            return False, "Epoch mismatch"

        return True, "CONSISTENCY_CERTIFIED"
