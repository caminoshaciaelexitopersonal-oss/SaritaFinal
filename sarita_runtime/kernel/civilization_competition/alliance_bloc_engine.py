class AllianceBlocEngine:
    def __init__(self):
        self.alliances = [] # List of sets of civ_ids

    def form_alliance(self, civ_ids):
        self.alliances.append(set(civ_ids))

    def get_allies(self, civ_id):
        allies = set()
        for alliance in self.alliances:
            if civ_id in alliance:
                allies.update(alliance)
        if civ_id in allies:
            allies.remove(civ_id)
        return allies

    def dissolve_alliances_with(self, civ_id):
        self.alliances = [a for a in self.alliances if civ_id not in a]
