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
