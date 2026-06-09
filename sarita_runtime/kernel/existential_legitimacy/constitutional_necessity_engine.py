class ConstitutionalNecessityEngine:
    """
    Engine that determines the necessity of SARITA's existence.
    """
    def __init__(self, validator, mapper, analyzer):
        self.validator = validator
        self.mapper = mapper
        self.analyzer = analyzer

    def verify_necessity(self, score: float):
        is_necessary = self.validator.validate_necessity(score)
        deps = self.mapper.map_dependencies()
        criticality = self.analyzer.analyze_criticality(deps)

        return {
            "is_necessary": is_necessary,
            "critical_dependencies": deps,
            "criticality_map": criticality
        }
