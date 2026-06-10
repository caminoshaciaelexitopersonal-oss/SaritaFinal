class MultiverseOutcomeAnalyzer:
    """
    Analyzes the total results of multiverse exploration.
    """
    def analyze_universe(self, universe):
        civ = universe["civilization"]
        final_state = civ.current_state

        return {
            "universe_id": universe["universe_id"],
            "meta_id": civ.meta_constitution.meta_id,
            "civilization": civ,
            "success": final_state["survival"] > 0.5,
            "generations": universe["generations_reached"],
            "final_metrics": final_state
        }

    def generate_report(self, outcomes):
        # Summarize outcomes
        total = len(outcomes)
        successful = sum(1 for o in outcomes if o["success"])
        avg_generations = sum(o["generations"] for o in outcomes) / total if total > 0 else 0

        report = f"# Constitutional Multiverse Report\n\n"
        report += f"Total Universes Explored: {total}\n"
        report += f"Successful Civilizations: {successful} ({successful/total*100:.2f}%)\n"
        report += f"Average Lifespan: {avg_generations:.2f} generations\n"
        report += f"Resilience Baseline: {sum(o['final_metrics']['resilience'] for o in outcomes)/total:.4f}\n"

        return report
