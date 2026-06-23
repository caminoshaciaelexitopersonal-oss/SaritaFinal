from sarita_runtime.kernel.civilizational_emergence.scientific_pluralism_engine import ScientificPluralismEngine

def run_demo():
    engine = ScientificPluralismEngine()
    print("Spawning rival schools of thought in Domain:GOVERNANCE...")
    factions = engine.spawn_rival_schools("GOVERNANCE", count=3)

    for f_id, data in factions.items():
        print(f"Faction: {f_id}, Paradigm: {data['paradigm']}, Support: {data['support']}")

    audit = engine.audit_pluralism()
    print(f"Pluralism Audit: {audit}")

if __name__ == "__main__":
    run_demo()
