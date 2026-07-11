class MetaAnalysisEngine:
    """
    Core manager that pulls studies, computes pooled combined effect sizes, heterogeneity metrics, and publication bias.
    """
    def __init__(self, study_aggregator, effect_combiner, heterogeneity_engine, bias_engine):
        self.study_aggregator = study_aggregator
        self.effect_combiner = effect_combiner
        self.heterogeneity_engine = heterogeneity_engine
        self.bias_engine = bias_engine

    def run_meta_analysis(self, study_ids: list) -> dict:
        studies = self.study_aggregator.aggregate_studies(study_ids)
        if not studies:
            return {"status": "NO_STUDIES", "combined_effect_size": 0.0}

        combined_effect = self.effect_combiner.combine_effects(studies)
        heterogeneity = self.heterogeneity_engine.calculate_heterogeneity(studies)
        pub_bias = self.bias_engine.evaluate_publication_bias(studies)

        return {
            "analyzed_studies_count": len(studies),
            "combined_effect_size": round(combined_effect, 4),
            "heterogeneity": heterogeneity,
            "publication_bias": pub_bias,
            "robustness_score": round(1.0 - heterogeneity["i_squared"], 4)
        }
