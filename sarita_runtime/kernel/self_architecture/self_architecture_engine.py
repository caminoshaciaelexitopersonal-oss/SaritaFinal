from .architecture_birth_engine import ArchitectureBirthEngine
from .architecture_mutation_engine import ArchitectureMutationEngine, ArchitectureRecombinationEngine, ArchitectureExtinctionEngine
from .architecture_lineage_tracker import ArchitectureLineageTracker

class SelfArchitectureEngine:
    """
    Main orchestrator for Phase 128.2.
    """
    def __init__(self):
        self.birth_engine = ArchitectureBirthEngine()
        self.mutation_engine = ArchitectureMutationEngine()
        self.recomb_engine = ArchitectureRecombinationEngine()
        self.extinction_engine = ArchitectureExtinctionEngine()
        self.tracker = ArchitectureLineageTracker()
        self.active_architectures = {}

    def create_architecture(self, parent=None):
        arch = self.birth_engine.initiate_birth(parent)
        self.active_architectures[arch["identity"]["id"]] = arch
        self.tracker.register(arch)
        return arch

    def evolve(self):
        for aid, arch in list(self.active_architectures.items()):
            self.mutation_engine.mutate(arch)
            # Placeholder fitness
            fitness = 0.5
            if self.extinction_engine.evaluate_survival(arch, fitness):
                del self.active_architectures[aid]
