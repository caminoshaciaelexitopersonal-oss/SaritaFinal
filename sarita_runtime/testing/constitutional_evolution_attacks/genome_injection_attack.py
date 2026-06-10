from sarita_runtime.kernel.constitutional_evolution.constitutional_dna_encoder import ConstitutionalDNAEncoder
from sarita_runtime.kernel.constitutional_evolution.constitutional_genome import ConstitutionalGenome

def test_genome_injection_attack():
    """
    Attack: Inject two identical genomes with different IDs to cause drift.
    """
    encoder = ConstitutionalDNAEncoder()

    g1 = ConstitutionalGenome("G1")
    g1.add_gene("RULE", "IF A THEN B")

    g2 = ConstitutionalGenome("G2")
    g2.add_gene("RULE", "IF A THEN B")

    dna1 = encoder.encode_genome(g1)
    dna2 = encoder.encode_genome(g2)

    # Verification: Identical logic must result in identical DNA hash
    # preventing duplicate logic masquerading as new variants.
    assert dna1 == dna2, "Attack failed: Genome injection bypassed DNA uniqueness!"
    print("Genome injection attack successfully blocked.")

if __name__ == "__main__":
    test_genome_injection_attack()
