import asyncio
import logging
import aiohttp
from aiohttp import web
import json
import uuid
import time

class FederatedTransportServer:
    """
    Real Federated Transport Server using aiohttp.
    Handles topology synchronization and epoch validation from peer clusters.
    """
    def __init__(self, registry):
        self.registry = registry

    async def start(self, port=8080):
        app = web.Application()
        app.router.add_post('/federation/v1/sync', self.handle_sync)
        app.router.add_get('/federation/v1/topology', self.handle_topology)
        runner = web.AppRunner(app)
        await runner.setup()
        site = web.TCPSite(runner, '0.0.0.0', port)
        await site.start()
        logging.info(f"Federated Transport Server (REAL) active on port {port}")

    async def handle_sync(self, request):
        try:
            data = await request.json()
            logging.info(f"Federation: Received sync from {data.get('cluster_id')}")
            # Process real bidirectional sync
            response = self.registry.handle_peer_sync(data)
            return web.json_response(response)
        except Exception as e:
            logging.error(f"Federation Server Error: {e}")
            return web.json_response({"status": "ERROR", "message": str(e)}, status=500)

    async def handle_topology(self, request):
        return web.json_response(self.registry.get_local_topology())

class FederatedTransportClient:
    """
    Real Federated Transport Client using aiohttp.
    Propagates local topology and state to remote clusters.
    """
    def __init__(self, peers):
        self.peers = peers
        self.session = None

    async def initialize(self):
        if not self.session:
            self.session = aiohttp.ClientSession()

    async def sync_with_peers(self, local_state):
        await self.initialize()
        results = []
        for peer in self.peers:
            try:
                # Real POST request to peer federation endpoint
                async with self.session.post(
                    f"{peer}/federation/v1/sync",
                    json=local_state,
                    timeout=5
                ) as resp:
                    if resp.status == 200:
                        peer_response = await resp.json()
                        results.append(peer_response)
                        logging.info(f"Federation: Peer {peer} ACK sync at epoch {peer_response.get('epoch')}")
            except Exception as e:
                logging.error(f"Federated Client: Peer {peer} connection failed: {e}")
        return results

    async def close(self):
        if self.session:
            await self.session.close()
