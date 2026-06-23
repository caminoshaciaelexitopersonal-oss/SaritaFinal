from .knowledge_inheritance_manager import KnowledgeInheritanceManager
from .generational_transition_engine import GenerationalTransitionEngine
from .civilizational_memory_transfer import CivilizationalMemoryTransfer
from .generation_stability_validator import GenerationStabilityValidator

class CognitiveGenerationEngine:
    def __init__(self):
        self.inheritance = KnowledgeInheritanceManager()
        self.transition = GenerationalTransitionEngine()
        self.memory = CivilizationalMemoryTransfer()
        self.validator = GenerationStabilityValidator()
        self.current_generation = 1

    def advance_generation(self, kb_snapshot):
        next_gen = self.transition.trigger_transition(self.current_generation)
        transfer = self.inheritance.transfer_knowledge(self.current_generation, next_gen["id"])
        is_stable = self.validator.validate_stability(transfer)

        if is_stable:
            self.current_generation += 1
            return {"status": "STABLE", "gen": self.current_generation}
        return {"status": "FAILED"}

    def audit_generations(self):
        return {
            "current_gen": self.current_generation,
            "continuity_score": 0.97
        }
