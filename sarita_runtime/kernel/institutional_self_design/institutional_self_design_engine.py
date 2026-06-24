from .governance_mutation_engine import GovernanceMutationEngine
from .constitutional_rewrite_engine import ConstitutionalRewriteEngine
from .institutional_recombination_engine import InstitutionalRecombinationEngine
from .adaptation_pressure_engine import AdaptationPressureEngine

class InstitutionalSelfDesignEngine:
    def __init__(self):
        self.gov_mutation = GovernanceMutationEngine()
        self.const_rewrite = ConstitutionalRewriteEngine()
        self.recombination = InstitutionalRecombinationEngine()
        self.pressure_engine = AdaptationPressureEngine()

    def redesign_institutions(self, civ, ecosystem_metrics):
        pressure = self.pressure_engine.calculate_pressure(civ, ecosystem_metrics)
        civ_id = civ["identity"]["id"]

        if pressure > 0.7:
            # High pressure leads to constitutional rewrite
            civ["genome"] = self.const_rewrite.rewrite_constitution(civ_id, civ["genome"])
        elif pressure > 0.4:
            # Moderate pressure leads to governance mutation
            civ["genome"] = self.gov_mutation.mutate_governance(civ["genome"])

        return civ["genome"]
