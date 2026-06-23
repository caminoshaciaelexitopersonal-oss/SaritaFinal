class ArchitecturalDeficitAnalyzer:
    """
    Analyzes the current architecture for rigidity, dependency on initial design, and obsolescence.
    """
    def analyze_architectural_deficits(self, kernel_state):
        deficits = []

        # Check for ME-1: Rigidity
        if kernel_state.get("is_fixed_topology", True):
            deficits.append("ME-1: High Architectural Rigidity")

        # Check for ME-2: Initial Design Dependency
        if kernel_state.get("uses_legacy_bootstrap", True):
            deficits.append("ME-2: Design Dependency")

        # Check for ME-3: Obsolescence
        if kernel_state.get("efficiency_metric", 1.0) < 0.7:
            deficits.append("ME-3: Architectural Obsolescence")

        return deficits
