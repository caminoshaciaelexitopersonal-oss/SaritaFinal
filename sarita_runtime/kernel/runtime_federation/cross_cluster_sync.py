import asyncio
import logging
import aiohttp

class CrossClusterSync:
    def __init__(self, registry, peers):
        self.registry = registry
        self.peers = peers # List of remote gateway URLs

    async def sync_loop(self):
        while True:
            await self.broadcast_state()
            await asyncio.sleep(10) # Epoch sync interval

    async def broadcast_state(self):
        state = self.registry.get_topology()
        async with aiohttp.ClientSession() as session:
            for peer in self.peers:
                try:
                    async with session.post(f"{peer}/federation/sync", json=state) as resp:
                        if resp.status == 200:
                            logging.info(f"Broadcast successful to {peer}")
                except Exception as e:
                    logging.error(f"Failed to sync with {peer}: {e}")
