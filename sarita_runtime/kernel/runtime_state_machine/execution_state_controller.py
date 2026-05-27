import logging
from enum import Enum

class ExecutionState(Enum):
    INIT = 0
    VERIFIED = 1
    EXECUTING = 2
    DEGRADED = 3
    FENCED = 4
    COLLAPSED = 5
    RECOVERING = 6

class ExecutionStateController:
    """
    Physical Runtime State Machine.
    Synchronous transitions to avoid asyncio critical path.
    """
    def __init__(self):
        self.current_state = ExecutionState.INIT

    def transition_to_sync(self, new_state: ExecutionState):
        logging.info(f"State Machine: PHYSICALLY TRANSITIONING {self.current_state.name} -> {new_state.name}")
        self.current_state = new_state
        return True

    async def transition_to(self, new_state: ExecutionState):
        return self.transition_to_sync(new_state)
