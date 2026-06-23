class ConstitutionalRuleInterpreter:
    """Interprets constitutional impact of evolutionary changes."""
    def interpret_constitutional_impact(self, proposal):
        impact_level = proposal.get("impact_level", 0.5)
        # Higher impact requires higher constitutional scrutiny
        score = 1.0 - (impact_level * 0.1)
        return {"score": score, "scrutiny_level": "HIGH" if impact_level > 0.7 else "NORMAL"}
