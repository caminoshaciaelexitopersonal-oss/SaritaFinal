import logging

class DeterministicRuntimeEpochMachine:
    """
    Coordinates runtime epochs with the physical state machine.
    """
    def __init__(self, state_controller):
        self.state_controller = state_controller
        self.current_epoch = 0

    async def start_epoch(self):
        if await self.state_controller.transition_to(ExecutionState.EXECUTING):
            self.current_epoch += 1
            logging.info(f"Epoch Machine: Epoch {self.current_epoch} STARTED.")
            return True
        return False

from sarita_runtime.kernel.runtime_state_machine.execution_state_controller import ExecutionState
