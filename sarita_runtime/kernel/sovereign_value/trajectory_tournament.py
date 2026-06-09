class TrajectoryTournament:
    """
    Conducts a "Tournament" between competing evolutionary trajectories.
    """
    def run_tournament(self, trajectories: list):
        # Pairwise competition
        winners = []
        for i in range(0, len(trajectories), 2):
            if i + 1 < len(trajectories):
                t1 = trajectories[i]
                t2 = trajectories[i+1]
                winner = t1 if t1["value"] > t2["value"] else t2
                winners.append(winner)
            else:
                winners.append(trajectories[i])
        return winners
