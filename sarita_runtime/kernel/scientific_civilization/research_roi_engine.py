class ResearchROIEngine:
    def calculate_roi(self, value, cost):
        return (value - cost) / cost if cost > 0 else value
