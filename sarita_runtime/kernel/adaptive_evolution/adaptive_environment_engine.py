class AdaptiveEnvironmentEngine:
    """
    Simulates and manages changing environmental conditions for constitutional testing.
    """
    def __init__(self, registry, pressure_model, stressor_generator):
        self.registry = registry
        self.pressure_model = pressure_model
        self.stressor_generator = stressor_generator

    def generate_environment_state(self, epoch_id):
        # Retrieve baseline and apply dynamic stressors
        base_state = self.registry.get_current_state()
        stressors = self.stressor_generator.generate_stressors(epoch_id)

        # Apply pressure model to derive final state
        return self.pressure_model.apply_pressures(base_state, stressors)
