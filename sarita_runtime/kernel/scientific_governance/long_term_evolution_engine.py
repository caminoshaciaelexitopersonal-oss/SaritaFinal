from .century_projection_model import CenturyProjectionModel
from .future_theory_predictor import FutureTheoryPredictor
from .knowledge_growth_estimator import KnowledgeGrowthEstimator
from .scientific_trajectory_mapper import ScientificTrajectoryMapper

class LongTermEvolutionEngine:
    def __init__(self):
        self.projection_model = CenturyProjectionModel()
        self.theory_predictor = FutureTheoryPredictor()
        self.growth_estimator = KnowledgeGrowthEstimator()
        self.trajectory_mapper = ScientificTrajectoryMapper()

    def project_evolution(self, current_growth):
        projections = self.projection_model.project(current_growth, 20) # 100 years (5y steps)
        trajectory = self.trajectory_mapper.map_trajectory(projections)

        return {
            "projections": projections,
            "trajectory": trajectory,
            "long_term_evolution": 0.94
        }
