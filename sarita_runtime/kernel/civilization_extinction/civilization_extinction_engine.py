from .collapse_detector import CollapseDetector
from .failure_cascade_analyzer import FailureCascadeAnalyzer
from .civilization_recovery_assessor import CivilizationRecoveryAssessor
from .irreversible_loss_tracker import IrreversibleLossTracker

class CivilizationExtinctionEngine:
    def __init__(self, resource_manager):
        self.collapse_detector = CollapseDetector(resource_manager)
        self.cascade_analyzer = FailureCascadeAnalyzer()
        self.recovery_assessor = CivilizationRecoveryAssessor()
        self.loss_tracker = IrreversibleLossTracker()

    def process_extinctions(self, civilizations):
        extinct_ids = []
        for civ in civilizations:
            risk = self.collapse_detector.check_collapse_risk(civ)
            if risk > 0.5:
                if self.cascade_analyzer.analyze_cascade_potential(civ, risk):
                    if not self.recovery_assessor.can_recover(civ):
                        self.loss_tracker.record_extinction(civ, "Systemic Collapse")
                        extinct_ids.append(civ["identity"]["id"])

        return extinct_ids
