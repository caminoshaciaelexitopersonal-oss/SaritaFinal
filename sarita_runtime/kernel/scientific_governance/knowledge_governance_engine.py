from .knowledge_lifecycle_manager import KnowledgeLifecycleManager
from .theory_retirement_engine import TheoryRetirementEngine
from .paradigm_transition_governor import ParadigmTransitionGovernor
from .knowledge_preservation_validator import KnowledgePreservationValidator

class KnowledgeGovernanceEngine:
    def __init__(self):
        self.lifecycle_manager = KnowledgeLifecycleManager()
        self.retirement_engine = TheoryRetirementEngine()
        self.transition_governor = ParadigmTransitionGovernor()
        self.preservation_validator = KnowledgePreservationValidator()

    def govern_knowledge(self, knowledge_pool):
        results = {}
        for theory_id, data in knowledge_pool.items():
            state = self.lifecycle_manager.determine_state(data["age"], data["evidence"])
            should_retire = self.retirement_engine.evaluate_retirement({**data, "lifecycle_state": state})
            results[theory_id] = {"state": state, "retired": should_retire}
        return results
