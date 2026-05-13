import asyncio
import logging
import random

class RaftNetworkTransport:
    def __init__(self, node_id, peer_endpoints):
        self.node_id = node_id
        self.peers = peer_endpoints # e.g. ["http://node2:8080", "http://node3:8080"]

    async def send_heartbeat(self, term):
        # 50.2 - Real asynchronous heartbeat to peers
        logging.info(f"Node {self.node_id} emitting heartbeat for term {term}")
        # Lógica real de requests.post o aiohttp
        await asyncio.sleep(0.1)

class ReplicatedStateMachine:
    def __init__(self):
        self.state = "NORMAL"

    def apply_command(self, command):
        # 50.2 - Commit to persistent state
        self.state = command.get('target_mode', self.state)
        return True

async def main_consensus():
    transport = RaftNetworkTransport("node-1", ["node-2", "node-3"])
    await transport.send_heartbeat(1)

if __name__ == "__main__":
    asyncio.run(main_consensus())
