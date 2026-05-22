import asyncio
import logging
import json
import time
import aiohttp
from aiohttp import web

class FederatedNodeRegistry:
    def __init__(self, cluster_id, region, peers):
        self.cluster_id = cluster_id
        self.region = region
        self.peers = peers # List of Peer URLs
        self.nodes = {}
        self.topology_hash = ""
        self.sync_epoch = 0
        self.session = None

    async def initialize(self):
        self.session = aiohttp.ClientSession()

    async def run_federation_sync(self):
        await self.initialize()
        while True:
            await self.broadcast_topology()
            await asyncio.sleep(15)

    async def broadcast_topology(self):
        payload = {
            "cluster_id": self.cluster_id,
            "region": self.region,
            "nodes": list(self.nodes.keys()),
            "epoch": self.sync_epoch,
            "timestamp": time.time()
        }

        for peer in self.peers:
            try:
                async with self.session.post(f"{peer}/federation/sync", json=payload, timeout=2) as resp:
                    if resp.status == 200:
                        data = await resp.json()
                        logging.info(f"Federation: Sync with {peer} successful. Peer epoch: {data.get('epoch')}")
            except Exception as e:
                logging.error(f"Federation: Failed to sync with {peer}: {e}")

    def handle_peer_sync(self, peer_data):
        peer_id = peer_data['cluster_id']
        self.nodes[peer_id] = peer_data
        self.sync_epoch += 1
        self._calculate_topology_hash()
        return {"status": "ACK", "epoch": self.sync_epoch}

    def _calculate_topology_hash(self):
        import hashlib
        topo = sorted(list(self.nodes.keys()) + [self.cluster_id])
        self.topology_hash = hashlib.sha256(json.dumps(topo).encode()).hexdigest()
        logging.info(f"Federation: New Topology Hash: {self.topology_hash}")

class FederationGateway:
    def __init__(self, registry):
        self.registry = registry

    async def start_server(self, port=8080):
        app = web.Application()
        app.router.add_post('/federation/sync', self.sync_handler)
        runner = web.AppRunner(app)
        await runner.setup()
        site = web.TCPSite(runner, '0.0.0.0', port)
        await site.start()
        logging.info(f"Federation Gateway listening on port {port}")

    async def sync_handler(self, request):
        data = await request.json()
        response = self.registry.handle_peer_sync(data)
        return web.json_response(response)
