import random

class CivilizationSpeciationEngine:
    def __init__(self, birth_engine):
        self.birth_engine = birth_engine
        self.speciation_threshold = 0.85

    def check_speciation_trigger(self, civ_id, environmental_pressure):
        civ = self.birth_engine.get_civilization(civ_id)
        if not civ:
            return False

        # Speciation occurs when environmental pressure or internal variance is high
        speciation_prob = (environmental_pressure * 0.5) + (random.random() * 0.5)
        return speciation_prob > self.speciation_threshold

    def speciate(self, parent_id):
        new_civ = self.birth_engine.birth_from_parent(parent_id)
        # Apply intense initial mutation to symbolize speciation event
        new_civ["genome"] = self.birth_engine.genome_builder.mutate_genome(new_civ["genome"], intensity=0.2)
        new_civ["status"] = "speciated"
        return new_civ
