import datetime

class LongitudinalResearchEngine:
    """
    Core engine that coordinates and manages longitudinal research studies over long execution timelines.
    """
    def __init__(self):
        self.studies = {}

    def start_study(self, study_id: str, description: str, variables: list) -> dict:
        self.studies[study_id] = {
            "description": description,
            "variables": variables,
            "started_at": datetime.datetime.now(datetime.timezone.utc).isoformat(),
            "time_points": []
        }
        return self.studies[study_id]

    def record_time_point(self, study_id: str, metrics: dict):
        if study_id in self.studies:
            self.studies[study_id]["time_points"].append({
                "timestamp": datetime.datetime.now(datetime.timezone.utc).isoformat(),
                "metrics": metrics
            })
