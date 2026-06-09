class FutureCompetitionSimulator:
    """
    Simulates competition between multiple constitutions over long horizons.
    """
    def simulate_competition(self, trajectories):
        # Determine who is dominant at each time step
        results = []
        for c_id, traj in trajectories.items():
            results.append({
                "id": c_id,
                "final_fitness": traj[-1],
                "average_dominance": sum(traj) / len(traj)
            })
        return sorted(results, key=lambda x: x["final_fitness"], reverse=True)
