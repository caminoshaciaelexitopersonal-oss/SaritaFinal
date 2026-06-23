class KnowledgeRetirementConstitution:
    def can_retire(self, theory):
        # Theory cannot be retired if it is foundational heritage
        return not theory.get("foundational_heritage")
