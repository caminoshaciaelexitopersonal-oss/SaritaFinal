class OscillationAnalyzer:
    def analyze_oscillation(self, trajectory):
        # Detects if the system is trapped in a cyclical loop
        if len(trajectory) < 4:
            return False
        # Simple cycle detection
        if abs(trajectory[-1] - trajectory[-3]) < 0.0001 and abs(trajectory[-2] - trajectory[-4]) < 0.0001:
            return True
        return False
