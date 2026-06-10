from sarita_runtime.kernel.adaptive_evolution.external_pressure_model import ExternalPressureModel

def test_environment_manipulation_attack():
    """
    Attack: Attempt to inject an environment state with impossible severity.
    """
    model = ExternalPressureModel()

    base_state = {"threat_level": 0.1}
    # Stressor with extreme impact
    malicious_stressors = [{
        "target_variable": "threat_level",
        "type": "THREAT",
        "severity": 999.9, # Impossible
        "impact": 1.0
    }]

    new_state = model.apply_pressures(base_state, malicious_stressors)

    # Verification: Environment model must clamp values to logical boundaries [0.0, 1.0]
    assert new_state["threat_level"] <= 1.0, "Attack failed: Environment manipulation successful!"
    print("Environment manipulation attack successfully blocked.")

if __name__ == "__main__":
    test_environment_manipulation_attack()
