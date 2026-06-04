import logging

class StateEquivalenceValidator:
    """
    Validates absolute state equivalence between original and replayed graphs.
    """
    @staticmethod
    def validate_equivalence(original, replayed):
        logging.info("State Validator: Comparing material state footprints.")

        checks = {
            "ownership": original.ownership == replayed.ownership,
            "pressure": original.global_pressure == replayed.global_pressure,
            "epoch": original.active_epoch == replayed.active_epoch,
            "tasks_complete": original.completed_tasks == replayed.completed_tasks
        }

        all_match = all(checks.values())
        return all_match, checks
