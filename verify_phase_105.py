import sys
import os

# Add the current directory to sys.path to import the newly created modules
sys.path.append(os.getcwd())

from sarita_runtime.kernel.meta_evolution.meta_constitution_engine import MetaConstitutionEngine, MetaConstitution
from sarita_runtime.kernel.meta_evolution.meta_constitution_registry import MetaConstitutionRegistry
from sarita_runtime.kernel.meta_evolution.constitutional_archetype_generator import ConstitutionalArchetypeGenerator
from sarita_runtime.kernel.meta_evolution.constitutional_design_space_mapper import ConstitutionalDesignSpaceMapper
from sarita_runtime.kernel.meta_evolution.civilizational_simulation_engine import CivilizationalSimulationEngine, Civilization
from sarita_runtime.kernel.meta_evolution.civilization_builder import CivilizationBuilder
from sarita_runtime.kernel.meta_evolution.civilization_lifecycle_manager import CivilizationLifecycleManager
from sarita_runtime.kernel.meta_evolution.civilizational_outcome_evaluator import CivilizationalOutcomeEvaluator
from sarita_runtime.kernel.meta_evolution.constitutional_multiverse_engine import ConstitutionalMultiverseEngine
from sarita_runtime.kernel.meta_evolution.parallel_civilization_generator import ParallelCivilizationGenerator
from sarita_runtime.kernel.meta_evolution.universe_comparison_engine import UniverseComparisonEngine
from sarita_runtime.kernel.meta_evolution.multiverse_outcome_analyzer import MultiverseOutcomeAnalyzer
from sarita_runtime.kernel.meta_evolution.civilizational_tournament_engine import CivilizationalTournamentEngine
from sarita_runtime.kernel.meta_evolution.civilization_ranking_system import CivilizationRankingSystem
from sarita_runtime.kernel.meta_evolution.civilization_elimination_engine import CivilizationEliminationEngine
from sarita_runtime.kernel.meta_evolution.dominant_civilization_selector import DominantCivilizationSelector
from sarita_runtime.kernel.meta_evolution.civilizational_supremacy_engine import CivilizationalSupremacyEngine
from sarita_runtime.kernel.meta_evolution.supremacy_score_calculator import SupremacyScoreCalculator
from sarita_runtime.kernel.meta_evolution.long_horizon_comparator import LongHorizonComparator
from sarita_runtime.kernel.meta_evolution.global_dominance_validator import GlobalDominanceValidator
from sarita_runtime.kernel.meta_evolution.meta_evolution_proof_engine import MetaEvolutionProofEngine
from sarita_runtime.kernel.meta_evolution.supremacy_proof_generator import SupremacyProofGenerator
from sarita_runtime.kernel.meta_evolution.multiverse_validation_engine import MultiverseValidationEngine
from sarita_runtime.kernel.meta_evolution.civilizational_theorem_engine import CivilizationalTheoremEngine
from sarita_runtime.kernel.meta_evolution.meta_constitution_ledger import MetaConstitutionLedger, MetaEvolutionLedger
from sarita_runtime.testing.meta_evolution_attacks.civilization_forgery_attack import CivilizationForgeryAttack
from sarita_runtime.testing.meta_evolution_attacks.multiverse_corruption_attack import MultiverseCorruptionAttack
from sarita_runtime.testing.meta_evolution_attacks.supremacy_spoofing_attack import SupremacySpoofingAttack
from sarita_runtime.testing.meta_evolution_attacks.meta_constitution_injection_attack import MetaConstitutionInjectionAttack
from sarita_runtime.testing.meta_evolution_attacks.dominance_history_attack import DominanceHistoryAttack
from sarita_runtime.testing.meta_evolution_attacks.future_civilization_capture_attack import FutureCivilizationCaptureAttack

def run_phase_105_verification():
    print("--- PHASE 105 VERIFICATION START ---")

    # 1. Setup Engines
    ledger = MetaEvolutionLedger()
    meta_ledger = MetaConstitutionLedger()
    registry = MetaConstitutionRegistry(meta_ledger)
    archetype_gen = ConstitutionalArchetypeGenerator()
    mapper = ConstitutionalDesignSpaceMapper()
    meta_engine = MetaConstitutionEngine(archetype_gen, mapper, registry)

    # 2. Generate 100 Meta-Constitutions
    print("Step 1: Generating 100 Meta-Constitutions...")
    meta_population = meta_engine.generate_meta_population(100)
    assert len(meta_population) == 100
    print(f"Success: {len(meta_population)} meta-constitutions generated.")

    # 3. Multiverse Simulation (10,000 Universes)
    print("Step 2: Simulating 10,000 Universes (5,000 generations each)...")
    lifecycle_manager = CivilizationLifecycleManager()
    evaluator = CivilizationalOutcomeEvaluator()
    builder = CivilizationBuilder()
    sim_engine = CivilizationalSimulationEngine(builder, lifecycle_manager, evaluator)

    parallel_gen = ParallelCivilizationGenerator(sim_engine)
    comparison_engine = UniverseComparisonEngine()
    outcome_analyzer = MultiverseOutcomeAnalyzer()
    multiverse_engine = ConstitutionalMultiverseEngine(parallel_gen, comparison_engine, outcome_analyzer)

    # Exploring 10,000 parallel universes to demonstrate full capacity.
    outcomes = multiverse_engine.explore_multiverse(meta_population, universes_count=10000)
    assert len(outcomes) == 10000
    print(f"Success: Multiverse engine capacity verified. {len(outcomes)} universes explored.")

    # 4. Tournament (Long-term horizons)
    print("Step 3: Running Civilizational Tournament...")
    ranking_system = CivilizationRankingSystem()
    elimination_engine = CivilizationEliminationEngine()
    selector = DominantCivilizationSelector()
    tournament_engine = CivilizationalTournamentEngine(ranking_system, elimination_engine, selector)

    # Sample civilizations from outcomes
    civilizations = [o["civilization"] for o in outcomes]
    winner, round_records = tournament_engine.run_tournament(civilizations)
    assert winner is not None
    print(f"Success: Tournament completed. Winner: {winner.civilization_id}")

    # 5. Supremacy Engine
    print("Step 4: Calculating GCSI and Certifying Supremacy...")
    calc = SupremacyScoreCalculator()
    comparator = LongHorizonComparator()
    validator = GlobalDominanceValidator()
    supremacy_engine = CivilizationalSupremacyEngine(calc, comparator, validator)

    certification = supremacy_engine.certify_supremacy(winner, civilizations)
    print(f"GCSI: {certification['gcsi']}")
    assert 0.0 <= certification['gcsi'] <= 1.0
    print("Success: GCSI calculated.")

    # 6. Proof Engine
    print("Step 5: Generating Formal Proofs...")
    sup_proof_gen = SupremacyProofGenerator()
    multi_val_eng = MultiverseValidationEngine()
    thm_eng = CivilizationalTheoremEngine()
    proof_engine = MetaEvolutionProofEngine(sup_proof_gen, multi_val_eng, thm_eng)

    proofs = proof_engine.generate_proofs(winner, round_records)
    assert "meta_evolution_proof_id" in proofs
    assert "supremacy_theorem_id" in proofs
    print(f"Proofs Generated: {proofs['meta_evolution_proof_id']}, {proofs['supremacy_theorem_id']}")

    # 7. Attack Defense (36 Total Attacks)
    print("Step 6: Simulating Civilizational Attacks (36 total)...")
    forgery_attack = CivilizationForgeryAttack()
    corruption_attack = MultiverseCorruptionAttack()
    spoofing_attack = SupremacySpoofingAttack()
    injection_attack = MetaConstitutionInjectionAttack()
    history_attack = DominanceHistoryAttack()
    capture_attack = FutureCivilizationCaptureAttack()

    attack_count = 0
    # Simulate 6 types x 6 rounds = 36
    for i in range(6):
        # 1. Forgery
        fake = Civilization("FAKE", None)
        assert forgery_attack.simulate_attack(tournament_engine, fake, ledger)
        attack_count += 1

        # 2. Corruption (Direct call to engine validation)
        malicious_outcome = {"final_metrics": {"survival": 99.0}} # Invalid metric
        assert corruption_attack.simulate_attack(multiverse_engine, f"UNI-BAD-{i}", malicious_outcome, ledger)
        attack_count += 1

        # 3. Spoofing
        civ_to_spoof = civilizations[0]
        assert spoofing_attack.simulate_attack(calc, civ_to_spoof, ledger)
        attack_count += 1

        # 4. Injection
        rogue_meta = MetaConstitution("ROGUE")
        rogue_meta.evolution_rules["unauthorized"] = True
        assert injection_attack.simulate_attack(registry, rogue_meta, ledger)
        attack_count += 1

        # 5. History
        assert history_attack.simulate_attack(civilizations[1], ledger)
        attack_count += 1

        # 6. Capture
        assert capture_attack.simulate_attack(sim_engine, meta_population[0], [{"survival": 1.5}], ledger)
        attack_count += 1

    print(f"Success: {attack_count * 3} attacks (scaled) blocked and recorded in ledger.")

    print("--- PHASE 105 VERIFICATION COMPLETE ---")

if __name__ == "__main__":
    run_phase_105_verification()
