class ConvergenceCertifier:
    def certify_convergence(self, is_fixed_point, is_oscillating):
        # Certifies that recursion is safe and stable
        return is_fixed_point and not is_oscillating
