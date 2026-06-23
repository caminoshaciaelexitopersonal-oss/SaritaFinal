class FixedPointDetector:
    def detect_fixed_point(self, trajectory, epsilon=0.0001):
        # Detects if a recursive state has reached a stable fixed point
        if len(trajectory) < 2:
            return False
        return abs(trajectory[-1] - trajectory[-2]) < epsilon
