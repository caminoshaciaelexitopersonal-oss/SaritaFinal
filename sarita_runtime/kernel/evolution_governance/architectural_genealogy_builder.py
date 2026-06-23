class ArchitecturalGenealogyBuilder:
    """Builds a genealogy map of architectural changes."""
    def build_genealogy(self, lineage):
        return {"root": lineage[-1], "leaf": lineage[0], "nodes": lineage}
