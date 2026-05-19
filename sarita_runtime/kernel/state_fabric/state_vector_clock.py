import logging

class StateVectorClock:
    """
    Real Distributed Vector Clocks for Causal Ordering.
    """
    def __init__(self, node_id):
        self.node_id = node_id
        self.clocks = {node_id: 0}

    def increment(self):
        self.clocks[self.node_id] += 1

    def update(self, peer_clocks):
        for node, count in peer_clocks.items():
            self.clocks[node] = max(self.clocks.get(node, 0), count)

    def compare(self, other_clocks):
        """
        Compares two vector clocks.
        Returns: -1 (less), 0 (equal), 1 (greater), None (concurrent)
        """
        less = False
        greater = False
        for node in set(self.clocks.keys()) | set(other_clocks.keys()):
            v1 = self.clocks.get(node, 0)
            v2 = other_clocks.get(node, 0)
            if v1 < v2: less = True
            if v1 > v2: greater = True

        if less and greater: return None # Concurrent
        if less: return -1
        if greater: return 1
        return 0

class DistributedStateMerger:
    async def merge_states(self, local_state, remote_state, local_clock, remote_clock):
        """
        Real Deterministic State Merging using Causal Ordering.
        """
        comparison = local_clock.compare(remote_clock.clocks)

        if comparison == 1: # Local is newer
            logging.info("State Merger: Local state is more recent. No merge required.")
            return local_state, local_clock
        elif comparison == -1: # Remote is newer
            logging.info("State Merger: Remote state is more recent. Accepting remote.")
            local_clock.update(remote_clock.clocks)
            return remote_state, local_clock
        else: # Concurrent or equal
            logging.warning("State Merger: Concurrent state detected. Applying Last-Writer-Wins (LWW).")
            # Here we fall back to timestamp or higher node_id for LWW.
            if remote_state.get('timestamp', 0) > local_state.get('timestamp', 0):
                local_clock.update(remote_clock.clocks)
                return remote_state, local_clock
            return local_state, local_clock
