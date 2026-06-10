from .constitutional_evolution_ledger import ConstitutionalEvolutionLedger

class ConstitutionalVariantLedger(ConstitutionalEvolutionLedger):
    """
    Ledger for recording constitutional variants and their genealogy.
    """
    def record_variant(self, variant):
        self._write({
            "type": "VARIANT_GENERATION",
            "variant_id": variant.genome_id,
            "parent_id": variant.parent_id
        })
