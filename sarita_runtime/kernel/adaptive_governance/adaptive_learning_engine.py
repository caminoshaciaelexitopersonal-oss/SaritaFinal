class AdaptiveLearningEngine:
    """
    Main engine for evolutionary learning from governance outcomes.
    """
    def __init__(self, experience_builder, failure_engine, pattern_extractor, ledger):
        self.experience_builder = experience_builder
        self.failure_engine = failure_engine
        self.pattern_extractor = pattern_extractor
        self.ledger = ledger

    def learn_from_iteration(self, actions, outcomes):
        """
        Learns from successes, failures, deviations, and anomalies.
        """
        experiences = [self.experience_builder.build_experience(a, o) for a, o in zip(actions, outcomes)]
        failures = [e for e in experiences if e["outcome"].get("success") is False]
        successes = [e for e in experiences if e["outcome"].get("success") is True]

        failure_lessons = [self.failure_engine.learn_from_failure(f) for f in failures]
        success_patterns = self.pattern_extractor.extract_patterns(successes)

        result = {
            "lessons_learned": len(failure_lessons),
            "patterns_extracted": len(success_patterns),
            "knowledge_base_delta": 0.05
        }

        if self.ledger:
            self.ledger.record_event("EVOLUTIONARY_LEARNING", result)

        return result
