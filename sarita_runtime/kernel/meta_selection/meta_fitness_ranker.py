class MetaFitnessRanker:
    def rank_meta_fitness(self, universes, performance_metrics):
        ranked = []
        for univ in universes:
            u_id = univ["identity"]["id"]
            perf = performance_metrics.get(u_id, 0.5)
            # Meta-fitness includes diversity contribution
            fitness = (perf * 0.7) + (univ["genome"].get("epistemic_stability", 0.5) * 0.3)
            ranked.append((univ, fitness))
        return sorted(ranked, key=lambda x: x[1], reverse=True)
