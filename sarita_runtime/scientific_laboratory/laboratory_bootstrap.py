class LaboratoryBootstrap:
    """
    Initializes registries, repositories, and sandboxes of the Scientific Laboratory.
    """
    def __init__(self, laboratory):
        self.lab = laboratory

    def boot(self):
        print("LaboratoryBootstrap: Initializing Scientific Laboratory space...")
        # Populate registries
        self.lab.experiments.register_experiment("EXP-001-COHESION", {"name": "Cohesion Optimization Trial"})
        self.lab.protocols.register_protocol("PRT-001-STRICT", {"name": "Strict Verification Protocol"})
        self.lab.benchmarks.register_benchmark("BENCH-001-BASE", {"cohesion": 0.85})
