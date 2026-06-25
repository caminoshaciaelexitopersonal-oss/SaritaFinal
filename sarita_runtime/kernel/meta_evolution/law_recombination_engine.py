import random

class LawRecombinationEngine:
    def recombine(self, laws_a, laws_b):
        new_laws = {}
        for law in laws_a:
            if law in laws_b:
                new_laws[law] = random.choice([laws_a[law], laws_b[law]])
            else:
                new_laws[law] = laws_a[law]
        return new_laws
