class ProductLifecycle:
    """
    Coordinates hooks and transitions for the product lifecycle states.
    States: INITIALIZED -> RUNNING -> ACTIVE -> TERMINATING -> OFFLINE.
    """
    def __init__(self, product):
        self.product = product
        self.state = "INITIALIZED"

    def transition_to(self, new_state: str):
        print(f"ProductLifecycle: Transitioning {self.state} -> {new_state}")
        self.state = new_state
        if new_state == "RUNNING":
            # Publish state change event if Event Bus is active
            pass
