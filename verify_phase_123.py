import sys
import os

sys.path.append(os.getcwd())

from sarita_runtime.kernel.civilizational_emergence.autonomous_institution_engine import AutonomousInstitutionEngine
from sarita_runtime.kernel.civilizational_emergence.scientific_pluralism_engine import ScientificPluralismEngine
from sarita_runtime.kernel.civilizational_emergence.constitutional_evolution_engine import EvolutionaryConstitutionalEngine
from sarita_runtime.kernel.civilizational_emergence.civilization_history_engine import CivilizationHistoryEngine
from sarita_runtime.kernel.civilizational_emergence.cognitive_generation_engine import CognitiveGenerationEngine
from sarita_runtime.kernel.civilizational_emergence.cognitive_government_engine import CognitiveGovernmentEngine
from sarita_runtime.kernel.civilizational_emergence.global_civilizational_emergence_index import GlobalCivilizationalEmergenceIndex

def verify():
    print("--- Phase 123: Civilizational Emergence & Institutional Pluralism Verification ---")

    engines = {
        "institution": AutonomousInstitutionEngine(),
        "pluralism": ScientificPluralismEngine(),
        "constitution": EvolutionaryConstitutionalEngine(),
        "history": CivilizationHistoryEngine(),
        "generation": CognitiveGenerationEngine(),
        "government": CognitiveGovernmentEngine()
    }

    # 1. Institutional Emergence
    print("[1] Verifying Autonomous Institution Spawning...")
    engines["institution"].spawn_institution("LOGIC", "Academy")
    engines["institution"].spawn_institution("PHYSICS", "Institute")
    audit_i = engines["institution"].audit_institutions()
    print(f"    Active Institutions: {audit_i['total_active']}")

    # 2. Scientific Pluralism
    print("[2] Verifying Scientific Pluralism...")
    engines["pluralism"].spawn_rival_schools("PHYSICS", count=3)
    audit_p = engines["pluralism"].audit_pluralism()
    print(f"    Pluralism Certified: {audit_p['is_plural']}")

    # 3. Constitutional Evolution
    print("[3] Verifying Constitutional Evolution...")
    engines["constitution"].apply_reform("RULE_X")
    audit_c = engines["constitution"].audit_constitutional_evolution()
    print(f"    Evolution Score: {audit_c['evolution_score']}")

    # 4. GCEI Calculation
    print("[4] Calculating Global Civilizational Emergence Index (GCEI)...")
    gcei_engine = GlobalCivilizationalEmergenceIndex(engines)
    gcei = gcei_engine.get_current_gcei()
    print(f"    GCEI Score: {gcei:.4f}")

    assert gcei > 0.9, f"GCEI {gcei} below acceptable threshold"
    print("\n✓ Phase 123 Verified Successfully. SARITA has reached Civilizational Emergence.")

if __name__ == "__main__":
    verify()
