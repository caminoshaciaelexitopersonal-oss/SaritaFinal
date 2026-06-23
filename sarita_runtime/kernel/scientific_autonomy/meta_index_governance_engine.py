from .index_reliability_estimator import IndexReliabilityEstimator
from .index_conflict_resolver import IndexConflictResolver
from .index_hierarchy_builder import IndexHierarchyBuilder
from .index_meta_validator import IndexMetaValidator

class MetaIndexGovernanceEngine:
    def __init__(self):
        self.reliability_estimator = IndexReliabilityEstimator()
        self.conflict_resolver = IndexConflictResolver()
        self.hierarchy_builder = IndexHierarchyBuilder()
        self.validator = IndexMetaValidator()
        self.priority_map = {"GSCI": 10, "GMCI": 9, "GRESI": 8, "GMEI": 7}

    def govern_indices(self, indices_data):
        reliabilities = {name: self.reliability_estimator.estimate_reliability(data["history"], data["evidence_quality"])
                         for name, data in indices_data.items()}
        hierarchy = self.hierarchy_builder.build_hierarchy(list(indices_data.keys()))

        return {
            "reliabilities": reliabilities,
            "hierarchy": hierarchy,
            "governance_status": "CERTIFIED"
        }
