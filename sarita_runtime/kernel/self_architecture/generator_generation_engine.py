from .engine_components import (
    EngineBuilder, EngineValidator, EngineOptimizer,
    EngineSpecializationEngine, EngineDeprecationManager, EngineCapabilityAnalyzer
)

class GeneratorGenerationEngine:
    """
    Orchestrates the generation of new engines. Phase 128.3.
    """
    def __init__(self):
        self.builder = EngineBuilder()
        self.validator = EngineValidator()
        self.optimizer = EngineOptimizer()
        self.specializer = EngineSpecializationEngine()
        self.deprecation = EngineDeprecationManager()
        self.analyzer = EngineCapabilityAnalyzer()
        self.engines = []

    def generate_engine(self, engine_type, spec):
        engine = self.builder.build_engine(engine_type, spec)
        if self.validator.validate(engine):
            engine = self.optimizer.optimize(engine)
            self.engines.append(engine)
            return engine
        return None

    def get_all_engines(self):
        return self.engines
