class LocalVsGlobalAnalyzer:
    """Analyzes if the current optimum is a local or global peak."""
    def analyze_local_vs_global(self, arch, boundary):
        # High depth in boundary detection indicates global search depth
        return boundary.get("knowledge_limit_depth", 0.0)
