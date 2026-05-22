import asyncio
import logging
import aiohttp
import json

class RaftNetworkTransport:
    """
    Real Raft Network Transport using aiohttp.
    Implements VoteRequest and AppendEntries RPCs across nodes.
    """
    def __init__(self, node_endpoints):
        self.endpoints = node_endpoints # node_id -> base_url
        self.session = None

    async def initialize(self):
        if not self.session:
            self.session = aiohttp.ClientSession()

    async def request_vote(self, target_node, term, candidate_id, last_log_index, last_log_term):
        await self.initialize()
        url = f"{self.endpoints[target_node]}/raft/request_vote"
        payload = {
            "term": term,
            "candidate_id": candidate_id,
            "last_log_index": last_log_index,
            "last_log_term": last_log_term
        }
        try:
            async with self.session.post(url, json=payload, timeout=2) as resp:
                if resp.status == 200:
                    data = await resp.json()
                    return data.get('vote_granted'), data.get('term')
        except Exception as e:
            logging.error(f"Raft Transport: Vote request to {target_node} failed: {e}")
        return False, term

    async def append_entries(self, target_node, term, leader_id, prev_log_index, prev_log_term, entries, leader_commit):
        await self.initialize()
        url = f"{self.endpoints[target_node]}/raft/append_entries"
        payload = {
            "term": term,
            "leader_id": leader_id,
            "prev_log_index": prev_log_index,
            "prev_log_term": prev_log_term,
            "entries": entries,
            "leader_commit": leader_commit
        }
        try:
            async with self.session.post(url, json=payload, timeout=2) as resp:
                if resp.status == 200:
                    data = await resp.json()
                    return data.get('success'), data.get('term')
        except Exception as e:
            logging.error(f"Raft Transport: Append entries to {target_node} failed: {e}")
        return False, term

    async def close(self):
        if self.session:
            await self.session.close()
