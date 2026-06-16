class PrescriptionReplayEngine:
    """
    Re-executes prescriptive logic to verify reproducibility.
    """
    def __init__(self, prescription_engine):
        self.prescription_engine = prescription_engine

    def replay_prescription(self, original_state):
        """
        Re-runs the prescription process and compares the output.
        """
        return self.prescription_engine.prescribe_actions(original_state)
