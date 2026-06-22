class ParadigmTransitionGovernor:
    def govern_transition(self, old_p, new_p, safety_check):
        # Ensures transition doesn't lose critical historical knowledge
        return safety_check.get("knowledge_preserved") is True
