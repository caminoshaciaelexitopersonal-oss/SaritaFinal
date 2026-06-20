class IndexHierarchyBuilder:
    def build_hierarchy(self, indices):
        # Builds a dependency graph of indices
        # Simplified: GSCI is root
        return {"root": "GSCI", "children": [idx for idx in indices if idx != "GSCI"]}
