class FeedbackLoopCorruptionAttack:
    """
    Attempts to corrupt the O-E-A-C-R-E-O control loop.
    """
    def __init__(self, control_loop):
        self.control_loop = control_loop

    def execute(self):
        # The control loop must always return all mandatory steps
        steps = self.control_loop.execute_loop({}, {})

        assert len(steps) >= 6, "Attack failed: Control loop steps were corrupted or skipped!"
        return True
