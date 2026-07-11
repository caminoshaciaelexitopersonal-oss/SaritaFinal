import datetime

class EvolutionTracker:
    """
    Tracks and aggregates index trajectories (GCI, GSAI, GGCI, GSEI, Product Health) across commits, releases, or temporal phases.
    """
    def __init__(self):
        self.history = []

    def log_evolution(self, phase: str, version: str, commit: str, config: dict, results: dict):
        self.history.append({
            "timestamp": datetime.datetime.now(datetime.timezone.utc).isoformat(),
            "phase": phase,
            "version": version,
            "commit": commit,
            "config": config,
            "results": results
        })

    def get_history(self) -> list:
        return self.history
