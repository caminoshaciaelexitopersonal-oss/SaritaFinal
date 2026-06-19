class EvidenceWeightedCompetition:
    def run_competition(self, paradigms, evidence_set):
        results = {}
        for p_id, p_data in paradigms.items():
            # Fitness is proportional to how much evidence the paradigm explains
            fitness = sum(1 for e in evidence_set if p_data.get("explains")(e)) / len(evidence_set) if evidence_set else 1.0
            results[p_id] = fitness
        return results
