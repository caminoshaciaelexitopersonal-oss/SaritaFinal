import uuid
import time
from .experience_memory import ExperienceMemory
from .execution_feedback_engine import ExecutionFeedbackEngine
from .policy_learning_engine import PolicyLearningEngine
from .knowledge_update_engine import KnowledgeUpdateEngine

class ContinuousLearningEngine:
    """
    Main manager for continuous cognitive optimization and learning.
    Translates raw executions into long-term system enhancements.
    """
    def __init__(self):
        self.memory = ExperienceMemory()
        self.feedback_engine = ExecutionFeedbackEngine()
        self.policy_engine = PolicyLearningEngine()
        self.knowledge_engine = KnowledgeUpdateEngine()

    def process_execution_outcome(self, execution_id: str, decision_node: dict, start_time: float, success: bool, rollback_triggered: bool, quality_delta: float) -> dict:
        """
        Processes the outcome of a controlled execution, updates weights and registers.
        """
        run_time = time.time() - start_time

        # Calculate mathematical feedback
        fb = self.feedback_engine.evaluate_feedback(run_time, success, rollback_triggered, quality_delta)

        # Save experience tuple
        state_before = {"status": "STABLE", "metrics": {"gaoi": 0.95}}
        state_after = {
            "status": "OPTIMIZED" if success else "REVERTED",
            "metrics": {
                "gaoi": 0.95 + (quality_delta if success else 0.0),
                "stability": fb["stability_impact"]
            }
        }

        self.memory.record_experience(
            action_id=execution_id,
            state_before=state_before,
            state_after=state_after,
            reward=fb["reward"],
            metadata={
                "decision_id": decision_node.get("decision_id"),
                "run_time_sec": run_time,
                "rollback_triggered": rollback_triggered
            }
        )

        # Update policy weights based on reward
        self.policy_engine.update_policy(fb["reward"], {
            "risk": decision_node.get("risk", 0.5),
            "benefit": decision_node.get("benefit", 0.5),
            "uncertainty": decision_node.get("uncertainty", 0.5),
            "priority": decision_node.get("priority", 0.5),
            "impact": decision_node.get("impact", 0.5)
        })

        # Update knowledge base
        self.knowledge_engine.integrate_knowledge(
            execution_id=execution_id,
            success=success,
            risk_level=decision_node.get("risk", 0.5),
            improvements=decision_node.get("alternatives", [])
        )

        return {
            "learning_id": f"LRN-{uuid.uuid4().hex[:8].upper()}",
            "reward": fb["reward"],
            "stability_impact": fb["stability_impact"],
            "performance_efficiency": fb["performance_efficiency"],
            "current_policy_weights": self.policy_engine.weights
        }
