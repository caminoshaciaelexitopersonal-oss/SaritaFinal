from .constitutional_evolution_ledger import ConstitutionalEvolutionLedger

class ConstitutionalGenomeLedger(ConstitutionalEvolutionLedger):
    """
    Ledger for recording all registered constitutional genomes and their DNA.
    """
    def record_genome(self, genome, dna_hash):
        self._write({
            "type": "GENOME_REGISTRATION",
            "genome_id": genome.genome_id,
            "dna_hash": dna_hash,
            "genes_count": len(genome.genes)
        })
