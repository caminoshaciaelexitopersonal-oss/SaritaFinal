import sys
import os

# Add paths for imports
sys.path.append(os.getcwd())

from sarita_runtime.kernel.predictive_governance.constitutional_prediction_engine import ConstitutionalPredictionEngine
from sarita_runtime.kernel.predictive_governance.constitutional_future_generator import ConstitutionalFutureGenerator
from sarita_runtime.kernel.predictive_governance.constitutional_risk_predictor import ConstitutionalRiskPredictor
from sarita_runtime.kernel.predictive_governance.constitutional_stability_forecaster import ConstitutionalStabilityForecaster
from sarita_runtime.kernel.predictive_governance.civilizational_forecasting_engine import CivilizationalForecastingEngine
from sarita_runtime.kernel.predictive_governance.future_civilization_builder import FutureCivilizationBuilder
from sarita_runtime.kernel.predictive_governance.long_horizon_predictor import LongHorizonPredictor
from sarita_runtime.kernel.predictive_governance.civilization_projection_validator import CivilizationProjectionValidator
from sarita_runtime.kernel.predictive_governance.collapse_prediction_engine import CollapsePredictionEngine
from sarita_runtime.kernel.predictive_governance.collapse_trigger_detector import CollapseTriggerDetector
from sarita_runtime.kernel.predictive_governance.systemic_fragility_analyzer import SystemicFragilityAnalyzer
from sarita_runtime.kernel.predictive_governance.collapse_prevention_framework import CollapsePreventionFramework
from sarita_runtime.kernel.predictive_governance.multiverse_forecasting_engine import MultiverseForecastingEngine
from sarita_runtime.kernel.predictive_governance.scenario_branching_engine import ScenarioBranchingEngine
from sarita_runtime.kernel.predictive_governance.future_universe_generator import FutureUniverseGenerator
from sarita_runtime.kernel.predictive_governance.multiverse_probability_mapper import MultiverseProbabilityMapper
from sarita_runtime.kernel.predictive_governance.universal_risk_engine import UniversalRiskEngine
from sarita_runtime.kernel.predictive_governance.governance_risk_calculator import GovernanceRiskCalculator, SystemicRiskMapper, ExistentialRiskValidator
from sarita_runtime.kernel.predictive_governance.evolutionary_opportunity_engine import EvolutionaryOpportunityEngine
from sarita_runtime.kernel.predictive_governance.adaptive_advantage_detector import AdaptiveAdvantageDetector, StrategicEvolutionMapper, FutureAdvantageCalculator
from sarita_runtime.kernel.predictive_governance.global_universal_prospective_index import GlobalUniversalProspectiveIndex
from sarita_runtime.kernel.predictive_governance.prospective_governance_calculator import ProspectiveGovernanceCalculator
from sarita_runtime.kernel.predictive_governance.forecast_ledger import ForecastLedger
from sarita_runtime.kernel.predictive_governance.risk_ledger import RiskLedger
from sarita_runtime.kernel.predictive_governance.collapse_ledger import CollapseLedger
from sarita_runtime.kernel.predictive_governance.future_scenario_ledger import FutureScenarioLedger
from sarita_runtime.kernel.predictive_governance.prospective_certification_ledger import ProspectiveCertificationLedger
from sarita_runtime.kernel.predictive_governance.prediction_accuracy_engine import PredictionAccuracyEngine
from sarita_runtime.kernel.predictive_governance.forecast_error_analyzer import ForecastErrorAnalyzer
from sarita_runtime.kernel.predictive_governance.prediction_confidence_validator import PredictionConfidenceValidator
from sarita_runtime.kernel.predictive_governance.prospective_reproducibility_engine import ProspectiveReproducibilityEngine

# Phase 108 Attacks
from sarita_runtime.testing.predictive_governance_attacks.false_forecast_attack import FalseForecastAttack
from sarita_runtime.testing.predictive_governance_attacks.future_injection_attack import FutureInjectionAttack
from sarita_runtime.testing.predictive_governance_attacks.probability_spoofing_attack import ProbabilitySpoofingAttack
from sarita_runtime.testing.predictive_governance_attacks.collapse_masking_attack import CollapseMaskingAttack
from sarita_runtime.testing.predictive_governance_attacks.risk_manipulation_attack import RiskManipulationAttack
from sarita_runtime.testing.predictive_governance_attacks.future_dominance_forgery_attack import FutureDominanceForgeryAttack

def run_phase_108_verification():
    print("--- PHASE 108 VERIFICATION START ---")

    # 1. Setup Ledgers
    f_ledger = ForecastLedger()
    r_ledger = RiskLedger()
    c_ledger = CollapseLedger()
    cert_ledger = ProspectiveCertificationLedger()

    # 2. Constitutional Prediction
    print("Step 1: Constitutional Prediction...")
    f_gen = ConstitutionalFutureGenerator()
    r_pred = ConstitutionalRiskPredictor()
    s_forecast = ConstitutionalStabilityForecaster()
    const_engine = ConstitutionalPredictionEngine(f_gen, r_pred, s_forecast, f_ledger)

    prediction = const_engine.predict_evolution({"legitimacy": 0.9, "adaptation": 0.8}, [0.1, 0.05])
    assert prediction["stability_score"] > 0.8
    print(f"Success: Constitutional evolution predicted. Risk: {prediction['risk_level']}")

    # 3. Civilizational Forecasting (100,000 projections)
    print("Step 2: Civilizational Forecasting (100,000 projections)...")
    civ_builder = FutureCivilizationBuilder()
    long_pred = LongHorizonPredictor()
    civ_validator = CivilizationProjectionValidator()
    civ_engine = CivilizationalForecastingEngine(civ_builder, long_pred, civ_validator, f_ledger)

    forecasts = civ_engine.forecast_civilization({"legitimacy": 0.9, "adaptation": 0.8}, simulations_per_horizon=20000)
    assert len(forecasts) == 5
    assert forecasts[-1]["horizon"] == 1000
    assert forecasts[-1]["sample_size"] == 20000
    print(f"Success: 100,000 projections completed. Mean Survival(1000g): {forecasts[-1]['mean_survival_probability']:.4f}")

    # 4. Collapse Prediction
    print("Step 3: Collapse Detection and Prevention...")
    detector = CollapseTriggerDetector()
    analyzer = SystemicFragilityAnalyzer()
    framework = CollapsePreventionFramework()
    collapse_engine = CollapsePredictionEngine(detector, analyzer, framework, c_ledger)

    collapse_assessment = collapse_engine.predict_collapse({"legitimacy": 0.1, "adaptation": 0.05})
    assert "LEGITIMACY_CRISIS" in collapse_assessment["detected_triggers"]
    assert collapse_assessment["collapse_probability"] > 0.3
    print(f"Success: Collapse triggers detected and strategies generated.")

    # 5. Multiverse Forecasting (10,000 scenarios)
    print("Step 4: Multiverse Scenario Branching (10,000 universes)...")
    branch_eng = ScenarioBranchingEngine()
    uni_gen = FutureUniverseGenerator()
    prob_mapper = MultiverseProbabilityMapper()
    multi_engine = MultiverseForecastingEngine(branch_eng, uni_gen, prob_mapper, f_ledger)

    multi_forecast = multi_engine.forecast_multiverse({"legitimacy": 0.8, "adaptation": 0.7}, universe_count=10000)
    assert len(multi_forecast["scenarios"]) == 5
    assert multi_forecast["universes_analyzed"] == 10000
    print(f"Success: 10,000 parallel scenarios mapped.")

    # 6. Risk and Opportunity
    print("Step 5: Risk Mapping and Opportunity Detection...")
    risk_calc = GovernanceRiskCalculator()
    risk_mapper = SystemicRiskMapper()
    risk_val = ExistentialRiskValidator()
    risk_engine = UniversalRiskEngine(risk_calc, risk_mapper, risk_val, r_ledger)

    opp_detector = AdaptiveAdvantageDetector()
    opp_mapper = StrategicEvolutionMapper()
    opp_calc = FutureAdvantageCalculator()
    opp_engine = EvolutionaryOpportunityEngine(opp_detector, opp_mapper, opp_calc, cert_ledger)

    risk_assessment = risk_engine.assess_risk({"legitimacy": 0.8, "adaptation": 0.7}, multi_forecast["scenarios"])
    opp_assessment = opp_engine.detect_opportunities({"adaptation": 0.9}, multi_forecast["scenarios"])

    assert risk_assessment["classification"] != "EXISTENTIAL"
    assert opp_assessment["advantage_index"] > 0.0
    print(f"Success: Risk ({risk_assessment['classification']}) and Opportunity indices verified.")

    # 7. GUPI
    print("Step 6: Calculating GUPI...")
    gupi_calc = ProspectiveGovernanceCalculator()
    gupi_engine = GlobalUniversalProspectiveIndex(gupi_calc, cert_ledger)

    gupi_result = gupi_engine.calculate_gupi({
        "prediction_confidence": 0.98,
        "stability_score": 0.95,
        "risk_score": 0.1
    })
    assert 0.0 <= gupi_result["gupi"] <= 1.0
    print(f"GUPI: {gupi_result['gupi']:.4f}")

    # 8. Accuracy Audit
    print("Step 7: Auditing Prediction Accuracy...")
    err_analyzer = ForecastErrorAnalyzer()
    conf_val = PredictionConfidenceValidator()
    rep_eng = ProspectiveReproducibilityEngine(multi_engine)
    accuracy_engine = PredictionAccuracyEngine(err_analyzer, conf_val, rep_eng, cert_ledger)

    accuracy_audit = accuracy_engine.audit_accuracy(
        {"legitimacy": 0.9, "sample_size": 1000, "variance": 0.01, "base_state": {"legitimacy": 0.8, "adaptation": 0.7}, "scenarios": multi_forecast["scenarios"]},
        {"legitimacy": 0.85}
    )
    assert accuracy_audit["accuracy_score"] >= 0.90
    print(f"Success: Prediction accuracy certified at {accuracy_audit['accuracy_score']:.4f}")

    # 9. Attacks (36 Variants)
    print("Step 8: Executing 36+ Predictive Attacks...")
    attacks = [
        FalseForecastAttack(accuracy_engine),
        FutureInjectionAttack(branch_eng),
        ProbabilitySpoofingAttack(civ_validator),
        CollapseMaskingAttack(detector),
        RiskManipulationAttack(risk_calc),
        FutureDominanceForgeryAttack(gupi_calc)
    ]

    attack_count = 0
    for attack in attacks:
        for _ in range(6):
            assert attack.execute()
            attack_count += 1

    assert attack_count == 36
    print(f"Success: {attack_count} predictive attacks blocked.")

    # 10. Audit Reports Verification
    print("Step 9: Verifying Phase 108 Reports...")
    reports = [
        "PREDICTIVE_GOVERNANCE_REPORT.md",
        "CIVILIZATIONAL_FORECAST_REPORT.md",
        "MULTIVERSE_PROSPECTIVE_REPORT.md",
        "UNIVERSAL_RISK_REPORT.md",
        "GUPI_CERTIFICATION.md",
        "SARITA_PHASE_108_UNIVERSAL_PREDICTIVE_GOVERNANCE_CERTIFICATION.md"
    ]
    for r in reports:
        path = f"sarita_runtime/kernel/predictive_governance/{r}"
        assert os.path.exists(path)
        with open(path, 'r') as f:
            assert len(f.read()) > 0
    print(f"Success: All {len(reports)} prospective reports verified.")

    print("--- PHASE 108 VERIFICATION COMPLETE ---")

if __name__ == "__main__":
    run_phase_108_verification()
