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
        # Summarize 10,000 universes
        total = len(outcomes)
        successful = sum(1 for o in outcomes if o["success"])

        report = f"# Constitutional Multiverse Report\n\n"
        report += f"Total Universes Explored: {total}\n"
        report += f"Successful Civilizations: {successful} ({successful/total*100:.2f}%)\n"
        # ... more details ...
        return report
