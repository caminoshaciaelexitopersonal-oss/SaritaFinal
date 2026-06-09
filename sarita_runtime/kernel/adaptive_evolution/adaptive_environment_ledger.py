from .adaptive_evolution_ledger import AdaptiveEvolutionLedger

class AdaptiveEnvironmentLedger(AdaptiveEvolutionLedger):
    """
    Ledger for recording environmental state transitions and stressors.
    """
    def record_environment_state(self, epoch_id, state):
        self._write({
            "type": "ENVIRONMENT_STATE",
            "epoch_id": epoch_id,
            "state_data": state
        })
