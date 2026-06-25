class OntologicalConflictResolver:
    def resolve_conflict(self, univ_a_concepts, univ_b_concepts):
        # Conflict is high if concept spaces are very different
        overlap = set(univ_a_concepts.keys()) & set(univ_b_concepts.keys())
        union = set(univ_a_concepts.keys()) | set(univ_b_concepts.keys())

        jaccard_similarity = len(overlap) / len(union) if union else 1.0
        conflict_intensity = 1.0 - jaccard_similarity

        return {
            "conflict_intensity": round(conflict_intensity, 4),
            "resolution_status": "Diverged" if conflict_intensity > 0.8 else "Convergent"
        }
