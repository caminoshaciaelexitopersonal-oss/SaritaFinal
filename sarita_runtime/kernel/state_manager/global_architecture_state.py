class GlobalArchitectureState:
    """
    Manages structural layout state, coupling degree, and technical debt.
    """
    def __init__(self):
        self.gsai = 0.9810
        self.coupling_degree = 0.120
        self.redundancy_ratio = 0.015
        self.module_count = 142

    def update_structure(self, gsai: float, coupling: float, redundancy: float):
        self.gsai = round(gsai, 4)
        self.coupling_degree = round(coupling, 4)
        self.redundancy_ratio = round(redundancy, 4)

    def to_dict(self) -> dict:
        return {
            "gsai": self.gsai,
            "coupling_degree": self.coupling_degree,
            "redundancy_ratio": self.redundancy_ratio,
            "module_count": self.module_count
        }
