import asyncio

class RuntimeStateManager:
    def __init__(self):
        self.global_state = "INITIALIZING"
        self.node_states = {}

    def set_system_mode(self, mode):
        # NORMAL, WAR_MODE, LOCKDOWN
        self.global_state = mode
        print(f"SYSTEM GLOBAL MODE changed to: {mode}")

    def update_node_state(self, node_id, state):
        self.node_states[node_id] = state
        print(f"Node {node_id} state converged to: {state}")

    def check_convergence(self):
        # Simple consensus check
        modes = set(self.node_states.values())
        if len(modes) == 1 and self.global_state in modes:
            return True
        return False

if __name__ == "__main__":
    sm = RuntimeStateManager()
    sm.update_node_state("node-1", "NORMAL")
    sm.update_node_state("node-2", "NORMAL")
    sm.set_system_mode("NORMAL")
    print(f"Converged: {sm.check_convergence()}")
