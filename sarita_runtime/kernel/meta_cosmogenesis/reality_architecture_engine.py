from .causality_architecture_builder import CausalityArchitectureBuilder
from .logic_framework_generator import LogicFrameworkGenerator
from .space_time_model_builder import SpaceTimeModelBuilder
from .reality_consistency_validator import RealityConsistencyValidator
from .constraint_system_generator import ConstraintSystemGenerator

class RealityArchitectureEngine:
    """
    Orchestrates the creation of reality architectures for a cosmos.
    Phase 127.3 - Reality Architecture Engine.
    """
    def __init__(self):
        self.causality_builder = CausalityArchitectureBuilder()
        self.logic_generator = LogicFrameworkGenerator()
        self.st_builder = SpaceTimeModelBuilder()
        self.validator = RealityConsistencyValidator()
        self.constraint_gen = ConstraintSystemGenerator()

    def design_reality(self, cosmos):
        genome = cosmos["genome"]

        causality = self.causality_builder.build_causality_model(genome["causality_linearity"])
        logic = self.logic_generator.generate_framework(genome["logical_entropy"])
        space_time = self.st_builder.build_model(genome["dimensionality"], genome["temporal_flow"])
        constraints = self.constraint_gen.generate_constraints(genome)

        architecture = {
            "causality": causality,
            "logic": logic,
            "space_time": space_time,
            "constraints": constraints
        }

        consistency_score = self.validator.validate(architecture)
        architecture["consistency_score"] = consistency_score

        cosmos["architecture"] = architecture
        return architecture
