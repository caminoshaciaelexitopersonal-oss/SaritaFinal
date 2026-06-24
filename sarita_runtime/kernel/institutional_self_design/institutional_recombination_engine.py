import random

class InstitutionalRecombinationEngine:
    def __init__(self):
        pass

    def recombine(self, genome_a, genome_b):
        new_genome = {}
        for trait in genome_a:
            if trait in genome_b:
                # Randomly pick from one parent or average
                choice = random.choice(["a", "b", "avg"])
                if choice == "a":
                    new_genome[trait] = genome_a[trait]
                elif choice == "b":
                    new_genome[trait] = genome_b[trait]
                else:
                    new_genome[trait] = round((genome_a[trait] + genome_b[trait]) / 2, 4)
            else:
                new_genome[trait] = genome_a[trait]
        return new_genome
