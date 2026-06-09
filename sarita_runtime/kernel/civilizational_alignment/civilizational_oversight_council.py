class CivilizationalOversightCouncil:
    """
    The ultimate oversight layer for civilizational alignment.
    """
    def __init__(self, chamber, adjudicator, guardian):
        self.chamber = chamber
        self.adjudicator = adjudicator
        self.guardian = guardian

    def perform_oversight(self, evolution: dict):
        purpose_ok, msg = self.chamber.review_purpose(evolution.get("purpose"))
        winner = self.adjudicator.adjudicate_conflict("Foundational_Unicity", "Adaptive_Efficiency")
        id_ok = self.guardian.protect_identity("SARITA_F1")

        verdict = purpose_ok and id_ok and (winner == "Foundational_Unicity")

        return {
            "verdict": "APPROVED" if verdict else "REJECTED",
            "oversight_summary": msg,
            "precedence_check": "FOUNDATIONAL_WINS"
        }
