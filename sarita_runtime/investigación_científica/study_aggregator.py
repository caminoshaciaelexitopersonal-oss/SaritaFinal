class StudyAggregator:
    """
    Aggregates historical scientific study results and trial effects.
    """
    def __init__(self):
        self.studies = {}

    def add_study(self, study_id: str, effect_size: float, variance: float, sample_size: int):
        self.studies[study_id] = {
            "study_id": study_id,
            "effect_size": effect_size,
            "variance": variance,
            "sample_size": sample_size
        }

    def aggregate_studies(self, study_ids: list) -> list:
        return [self.studies[sid] for sid in study_ids if sid in self.studies]
