class FutureStateDesigner:
    """
    Designs the objective future state for a civilization.
    """
    def design_state(self, optimized_path):
        """
        Translates a path into a detailed architectural state design.
        """
        return {
            "design_id": f"DESIGN-{optimized_path['id']}",
            "metrics_target": {"legitimacy": 0.98, "stability": 0.97}
        }
