import json
import os

class PerformanceHistory:
    """
    Maintains a physical json-backed log on disk of performance metrics over long evaluation horizons.
    """
    def __init__(self, log_path: str = "performance_history.json"):
        self.log_path = log_path
        self.history_records = []
        self.load_history()

    def load_history(self):
        if os.path.exists(self.log_path):
            try:
                with open(self.log_path, "r") as f:
                    self.history_records = json.load(f)
            except Exception:
                self.history_records = []

    def record_run(self, date_str: str, phase: str, version: str, commit_hash: str, config: dict, results: dict):
        self.history_records.append({
            "date": date_str,
            "phase": phase,
            "version": version,
            "commit": commit_hash,
            "config": config,
            "results": results
        })
        self.save_history()

    def save_history(self):
        try:
            with open(self.log_path, "w") as f:
                json.dump(self.history_records, f, indent=4)
        except Exception:
            pass

    def get_all_records(self) -> list:
        return self.history_records
