class ParadigmSocietyManager:
    def __init__(self):
        self.factions = {}

    def add_faction(self, faction):
        self.factions[faction["id"]] = faction

    def get_distribution(self):
        return self.factions
