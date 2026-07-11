class ExternalValidationProtocol:
    """
    Enforces the independent verification process by forcing third-party run validations without using previous cached state.
    """
    def __init__(self):
        pass

    def perform_external_audit(self, independent_runner_func, benchmark_val: float) -> dict:
        observed = independent_runner_func()
        difference = abs(observed - benchmark_val)
        success = difference < 0.05
        return {
            "external_observed_value": round(observed, 4),
            "expected_reference_value": round(benchmark_val, 4),
            "absolute_deviation": round(difference, 4),
            "audit_passed": success
        }
