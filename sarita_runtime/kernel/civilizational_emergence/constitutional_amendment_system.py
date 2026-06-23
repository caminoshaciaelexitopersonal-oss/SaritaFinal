class ConstitutionalAmendmentSystem:
    def propose_amendment(self, constitution, new_rule):
        # Proposes a modification to an active constitution
        return {
            "id": f"AMD-{hash(new_rule)%1000}",
            "base_constitution": constitution["id"],
            "new_rule": new_rule,
            "status": "PROPOSED"
        }
