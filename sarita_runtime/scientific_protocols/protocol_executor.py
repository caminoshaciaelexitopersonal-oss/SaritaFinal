class ProtocolExecutor:
    """
    Executes a formal scientific protocol and collects raw observation arrays.
    """
    def __init__(self):
        pass

    def execute(self, protocol, action_callable) -> dict:
        observations = []
        for i in range(protocol.repetitions):
            # Run trial callable
            res = action_callable(i)
            observations.append(res)

        return {
            "protocol_name": protocol.name,
            "trials_run": len(observations),
            "observations": observations
        }
