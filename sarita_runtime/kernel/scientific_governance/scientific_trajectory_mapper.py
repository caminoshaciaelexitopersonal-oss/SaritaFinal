class ScientificTrajectoryMapper:
    def map_trajectory(self, projections):
        # Maps future milestones on a trajectory
        return [{"year": 5 * i, "milestone": f"LEVEL_{i}"} for i in range(len(projections))]
