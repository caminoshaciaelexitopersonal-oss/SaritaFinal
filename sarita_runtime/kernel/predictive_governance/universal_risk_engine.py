class UniversalRiskEngine:
    """
    Engine for calculating and mapping universal governance risks.
    """
    def __init__(self, calculator, mapper, validator, ledger):
        self.calculator = calculator
        self.mapper = mapper
        self.validator = validator
        self.ledger = ledger

    def assess_risk(self, system_state, scenarios):
        """
        Performs a comprehensive risk assessment (LOW to EXISTENTIAL).
        """
        raw_risk = self.calculator.calculate_risk(system_state)
        risk_map = self.mapper.map_systemic_risk(scenarios)

        # Determine classification
        classification = self._classify_risk(raw_risk)

        assessment = {
            "risk_score": raw_risk,
            "classification": classification,
            "risk_map": risk_map,
            "is_valid": self.validator.validate_risk(raw_risk)
        }

        if self.ledger:
            self.ledger.record_risk_assessment(assessment)

        return assessment

    def _classify_risk(self, score):
        if score > 0.9: return "EXISTENTIAL"
        if score > 0.8: return "CRITICAL"
        if score > 0.6: return "SEVERE"
        if score > 0.4: return "HIGH"
        if score > 0.2: return "MODERATE"
        return "LOW"
class EvolutionaryOpportunityEngine:
    """
    Engine for detecting evolutionary opportunities and adaptive advantages.
    """
    def __init__(self, detector, mapper, calculator, ledger):
        self.detector = detector
        self.mapper = mapper
        self.calculator = calculator
        self.ledger = ledger

    def detect_opportunities(self, current_state, future_scenarios):
        """
        Detects opportunities for adaptation, growth, and supremacy.
        """
        raw_ops = self.detector.detect_advantage(current_state)
        strat_map = self.mapper.map_strategic_evolution(future_scenarios)

        assessment = {
            "opportunities": raw_ops,
            "strategic_map": strat_map,
            "advantage_index": self.calculator.calculate_future_advantage(raw_ops)
        }

        if self.ledger:
            self.ledger.record_opportunity_assessment(assessment)

        return assessment
