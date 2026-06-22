class ScientificROICalculator:
    def calculate_roi(self, investment, knowledge_gain):
        # Simple ROI: knowledge gain divided by cognitive investment
        return knowledge_gain / investment if investment > 0 else 0.0
