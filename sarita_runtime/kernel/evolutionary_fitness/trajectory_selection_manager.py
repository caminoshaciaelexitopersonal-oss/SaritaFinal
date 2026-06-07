class TrajectorySelectionManager:
    """
    Manages the selection of evolutionary trajectories based on fitness.
    """
    def select_best_trajectory(self, trajectories: list):
        if not trajectories:
            return None
        return max(trajectories, key=lambda x: x["fitness"])
