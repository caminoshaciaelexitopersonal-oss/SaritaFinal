import random
from .institution_birth_engine import InstitutionBirthEngine
from .institution_growth_engine import InstitutionGrowthEngine
from .institution_decline_engine import InstitutionDeclineEngine
from .institution_extinction_engine import InstitutionExtinctionEngine
from .institution_ecosystem_mapper import InstitutionEcosystemMapper

class InstitutionalEcosystemEngine:
    def __init__(self):
        self.birth_engine = InstitutionBirthEngine()
        self.growth_engine = InstitutionGrowthEngine()
        self.decline_engine = InstitutionDeclineEngine()
        self.extinction_engine = InstitutionExtinctionEngine()
        self.mapper = InstitutionEcosystemMapper()
        self.institutions = []

    def process_cycle(self, environmental_resources):
        if random.random() < 0.1:
            self.institutions.append(self.birth_engine.trigger_birth(None))

        active_institutions = []
        for inst in self.institutions:
            if inst["status"] == "EXTINCT":
                continue

            if environmental_resources > 0.5:
                self.growth_engine.evolve(inst, environmental_resources)
            else:
                self.decline_engine.decline(inst)

            if inst["resources"] > 5.0:
                inst["resources"] /= 2
                active_institutions.append(self.birth_engine.trigger_birth(None))

            if not self.extinction_engine.check_extinction(inst):
                active_institutions.append(inst)

        self.institutions = active_institutions
        return self.mapper.map_relationships(self.institutions)

    def get_metrics(self):
        return {
            "count": len(self.institutions),
            "total_resources": sum(i["resources"] for i in self.institutions),
            "average_fitness": sum(i["fitness"] for i in self.institutions) / len(self.institutions) if self.institutions else 0
        }
