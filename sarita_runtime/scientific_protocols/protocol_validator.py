class ProtocolValidator:
    """
    Validates that a Protocol contains all mandatory scientific fields.
    """
    def __init__(self):
        pass

    def validate_protocol(self, protocol) -> dict:
        errors = []
        if not protocol.hypothesis:
            errors.append("Hypothesis statement is empty.")
        if not protocol.control_variables:
            errors.append("Control variables are empty.")
        if not protocol.independent_variables:
            errors.append("Independent variables are empty.")
        if not protocol.dependent_variables:
            errors.append("Dependent variables are empty.")
        if protocol.repetitions <= 0:
            errors.append("Repetitions must be greater than zero.")

        return {
            "valid": len(errors) == 0,
            "errors": errors
        }
