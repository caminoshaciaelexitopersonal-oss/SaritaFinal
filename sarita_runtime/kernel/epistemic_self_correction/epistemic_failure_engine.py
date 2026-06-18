from .epistemic_failure_ledger import EpistemicFailureLedger
from .reasoning_failure_analyzer import ReasoningFailureAnalyzer
from .error_pattern_detector import ErrorPatternDetector
from .lesson_extractor import LessonExtractor

class EpistemicFailureEngine:
    def __init__(self):
        self.ledger = EpistemicFailureLedger()
        self.analyzer = ReasoningFailureAnalyzer()
        self.pattern_detector = ErrorPatternDetector()
        self.extractor = LessonExtractor()
        self.failure_history = []

    def record_and_learn(self, failure_id, reasoning_path, actual_outcome):
        analysis = self.analyzer.analyze_failure(reasoning_path, actual_outcome)
        self.failure_history.append({"id": failure_id, "type": "LOGICAL_DIVERGENCE", "analysis": analysis})

        patterns = self.pattern_detector.detect_patterns(self.failure_history)
        lesson = self.extractor.extract_lesson(analysis, patterns)

        self.ledger.record_failure(
            failure_id=failure_id,
            failure_type="LOGICAL_DIVERGENCE",
            analysis=analysis,
            lesson_learned=lesson
        )
        return lesson
