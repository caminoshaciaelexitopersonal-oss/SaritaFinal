class ConstitutionalIntelligenceCore:
    """
    The central intelligence unit for meta-constitutional reasoning.
    """
    def __init__(self):
        self.meta_knowledge = {}

    def update_meta_knowledge(self, domain: str, knowledge: dict):
        self.meta_knowledge[domain] = knowledge

    def get_meta_guidance(self, domain: str):
        return self.meta_knowledge.get(domain, {})
