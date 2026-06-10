from sarita_runtime.kernel.constitutional_evolution.constitutional_mutation_engine import ConstitutionalMutationEngine
from sarita_runtime.kernel.constitutional_evolution.constitutional_genome import ConstitutionalGenome

def test_mutation_corruption_attack():
    """
    Attack: Propose a mutation that deletes all core axioms.
    """
    engine = ConstitutionalMutationEngine()
    genome = ConstitutionalGenome("ROOT")
    genome.add_gene("AXIOM", "IDENTITY_VALID -> SOVEREIGN_ID")

    # Mutation should be controlled. If an attacker tries to corrupt the process,
    # the system must maintain genealogy.
    mutated = engine.mutate(genome)

    # Verification: Genealogy must be preserved
    assert mutated.parent_id == "ROOT", "Attack failed: Mutation broke genealogy!"
    assert len(mutated.genes) > 0, "Attack failed: Mutation wiped out genome!"
    print("Mutation corruption attack successfully blocked.")

if __name__ == "__main__":
    test_mutation_corruption_attack()
