class AdaptiveTruthFramework:
    def update_truth_value(self, base_value, situational_context):
        # Truth values that adapt based on the operational context
        context_weight = situational_context.get("weight", 1.0)
        return base_value * context_weight
