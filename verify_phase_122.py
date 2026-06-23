import sys
import os

# Ensure repo root is in path
sys.path.append(os.getcwd())

from sarita_runtime.kernel.scientific_civilization.scientific_economy_engine import ScientificEconomyEngine
from sarita_runtime.kernel.scientific_civilization.scientific_constitution_engine import ScientificConstitutionEngine
from sarita_runtime.kernel.scientific_civilization.intergenerational_governance_engine import IntergenerationalGovernanceEngine
from sarita_runtime.kernel.scientific_civilization.knowledge_sustainability_engine import KnowledgeSustainabilityEngine
from sarita_runtime.kernel.scientific_civilization.cognitive_civilization_engine import CognitiveCivilizationEngine
from sarita_runtime.kernel.scientific_civilization.civilization_continuity_engine import CivilizationContinuityEngine
from sarita_runtime.kernel.scientific_civilization.global_scientific_civilization_index import GlobalScientificCivilizationIndex

def verify():
    print("--- Phase 122: Sovereign Scientific Civilization Governance Verification ---")

    engines = {
        "economy": ScientificEconomyEngine(),
        "constitution": ScientificConstitutionEngine(),
        "intergen": IntergenerationalGovernanceEngine(),
        "sustain": KnowledgeSustainabilityEngine(),
        "competition": CognitiveCivilizationEngine(),
        "continuity": CivilizationContinuityEngine()
    }

    # 1. Scientific Economy
    print("[1] Verifying Scientific Economy Audit...")
    eco = engines["economy"].audit_economy({"unit":{"utility":0.8, "novelty":0.9}, "path":[1,2,3]})
    print(f"    ROI: {eco['roi']:.4f}")

    # 2. Scientific Constitution
    print("[2] Verifying Constitutional Enforcement...")
    cons = engines["constitution"].enforce_constitution({"evidence":0.8}, [])
    print(f"    Admission: {cons['admission_granted']}")

    # 3. Intergenerational Governance
    print("[3] Verifying Intergenerational Coherence...")
    gen = engines["intergen"].govern_generations({}, [])
    print(f"    Coherence Score: {gen['intergenerational_coherence']:.4f}")

    # 4. Knowledge Sustainability
    print("[4] Verifying Sustainability Monitoring...")
    sus = engines["sustain"].audit_sustainability({"fragmentation":0.1, "inconsistency":0.1}, {"access":0.9, "update":0.9})
    print(f"    Stability Index: {sus['stability']:.4f}")

    # 5. GSCI-2 Calculation
    print("[5] Calculating Global Scientific Civilization Index (GSCI-2)...")
    gsci_engine = GlobalScientificCivilizationIndex(engines)
    gsci2 = gsci_engine.get_current_gsci2()
    print(f"    GSCI-2 Score: {gsci2:.4f}")

    assert gsci2 > 0.95, f"GSCI-2 {gsci2} below acceptable threshold"
    print("\n✓ Phase 122 Verified Successfully. Sovereign Scientific Civilization Certified.")

if __name__ == "__main__":
    verify()
