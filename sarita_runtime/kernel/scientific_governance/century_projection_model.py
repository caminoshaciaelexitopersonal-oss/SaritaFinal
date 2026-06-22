class CenturyProjectionModel:
    def project(self, current_growth, steps):
        # Projects knowledge growth over decades (steps)
        return [current_growth * (1.05 ** i) for i in range(steps)]
