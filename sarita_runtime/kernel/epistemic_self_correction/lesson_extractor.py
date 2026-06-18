class LessonExtractor:
    def extract_lesson(self, failure_analysis, pattern_data):
        # Converts patterns into actionable governance constraints
        return {
            "constraint": f"INCREASE_VIGILANCE_ON_{failure_analysis.get('failure_node')}",
            "impact": "REDUCED_RECURRENCE_PROBABILITY"
        }
