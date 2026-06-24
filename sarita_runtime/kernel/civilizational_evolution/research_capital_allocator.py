class ResearchCapitalAllocator:
    def allocate(self, institution, amount):
        institution["research_capital"] = institution.get("research_capital", 0) + amount
