class MetaConstitutionalCourt:
    """
    High-level court that judges the quality and evolutionary value of reforms.
    Unlike the standard court, this one focuses on WISDOM and META-OPTIMIZATION.
    """
    def __init__(self, assessment_engine, quality_validator, intelligence_core):
        self.assessment_engine = assessment_engine
        self.quality_validator = quality_validator
        self.intelligence_core = intelligence_core
        self.verdicts = {}

    def judge_reform_quality(self, reform: dict, history_metrics: list):
        # 1. Assess evolutionary value
        evo_value = self.assessment_engine.assess_evolutionary_value(reform, history_metrics)

        # 2. Validate governance quality
        quality_ok, reason = self.quality_validator.validate_quality(reform, self.intelligence_core)

        verdict = (evo_value > 0.7) and quality_ok

        self.verdicts[reform.get("id")] = {
            "verdict": "APPROVED" if verdict else "REJECTED",
            "evo_value": evo_value,
            "quality_ok": quality_ok,
            "reason": reason
        }

        return verdict
