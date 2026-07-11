class ProtocolAuditor:
    """
    Audits the execution logs of protocols to find deviations from scientific designs.
    """
    def __init__(self):
        pass

    def audit_execution(self, protocol_dict: dict, execution_res: dict) -> dict:
        deviations = []
        if execution_res.get("trials_run", 0) != protocol_dict.get("repetitions", 10):
            deviations.append("Mismatched trial repetition count!")

        return {
            "compliant": len(deviations) == 0,
            "deviations": deviations
        }
