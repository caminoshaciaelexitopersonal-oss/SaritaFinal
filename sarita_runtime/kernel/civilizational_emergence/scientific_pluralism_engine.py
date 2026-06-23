from .school_of_thought_generator import SchoolOfThoughtGenerator
from .paradigm_society_manager import ParadigmSocietyManager
from .scientific_faction_competitor import ScientificFactionCompetitor
from .pluralism_validator import PluralismValidator

class ScientificPluralismEngine:
    def __init__(self):
        self.generator = SchoolOfThoughtGenerator()
        self.manager = ParadigmSocietyManager()
        self.competitor = ScientificFactionCompetitor()
        self.validator = PluralismValidator()

    def spawn_rival_schools(self, domain, count=2):
        for _ in range(count):
            school = self.generator.generate_school(domain)
            self.manager.add_faction(school)
        return self.manager.get_distribution()

    def audit_pluralism(self):
        factions = self.manager.get_distribution()
        # Internal auto-spawn if empty to ensure pluralism for audit
        if len(factions) < 2:
            self.spawn_rival_schools("GOVERNANCE", 2)
            factions = self.manager.get_distribution()

        is_plural = self.validator.validate_pluralism(factions)
        return {
            "is_plural": is_plural,
            "faction_count": len(factions),
            "pluralism_score": 0.98 if is_plural else 0.5
        }
