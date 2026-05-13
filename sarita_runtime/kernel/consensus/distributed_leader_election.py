import asyncio
import logging
import random
import time
import json

class RaftNode:
    def __init__(self, node_id, peers, transport, storage):
        self.node_id = node_id
        self.peers = peers
        self.transport = transport
        self.storage = storage

        # Persistent state
        self.current_term = self.storage.get("current_term", 0)
        self.voted_for = self.storage.get("voted_for", None)
        self.log = self.storage.get("log", [])

        # Volatile state
        self.commit_index = 0
        self.last_applied = 0
        self.state = "FOLLOWER"
        self.leader_id = None

        # Volatile state on leaders
        self.next_index = {peer: len(self.log) for peer in peers}
        self.match_index = {peer: 0 for peer in peers}

        self.election_timeout = random.uniform(1.5, 3.0)
        self.last_heartbeat = time.time()

    async def run(self):
        while True:
            if self.state == "FOLLOWER" or self.state == "CANDIDATE":
                if time.time() - self.last_heartbeat > self.election_timeout:
                    await self.start_election()
            elif self.state == "LEADER":
                await self.send_append_entries()
            await asyncio.sleep(0.1)

    async def start_election(self):
        self.state = "CANDIDATE"
        self.current_term += 1
        self.voted_for = self.node_id
        self.last_heartbeat = time.time()
        self.election_timeout = random.uniform(1.5, 3.0)

        votes = 1
        logging.info(f"Node {self.node_id} starting election for term {self.current_term}")

        for peer in self.peers:
            if await self.transport.request_vote(peer, self.current_term, self.node_id, len(self.log)-1, self.log[-1]['term'] if self.log else 0):
                votes += 1

        if votes > (len(self.peers) + 1) / 2:
            await self.become_leader()

    async def become_leader(self):
        self.state = "LEADER"
        self.leader_id = self.node_id
        logging.info(f"Node {self.node_id} became LEADER for term {self.current_term}")
        for peer in self.peers:
            self.next_index[peer] = len(self.log)
            self.match_index[peer] = 0

    async def send_append_entries(self):
        for peer in self.peers:
            prev_index = self.next_index[peer] - 1
            prev_term = self.log[prev_index]['term'] if prev_index >= 0 else 0
            entries = self.log[self.next_index[peer]:]

            success, term = await self.transport.append_entries(
                peer, self.current_term, self.node_id, prev_index, prev_term, entries, self.commit_index
            )

            if success:
                self.next_index[peer] = len(self.log)
                self.match_index[peer] = len(self.log) - 1
                await self.update_commit_index()
            elif term > self.current_term:
                await self.step_down(term)
            else:
                self.next_index[peer] = max(0, self.next_index[peer] - 1)

    async def update_commit_index(self):
        for n in range(len(self.log) - 1, self.commit_index, -1):
            if self.log[n]['term'] == self.current_term:
                count = 1
                for peer in self.peers:
                    if self.match_index[peer] >= n:
                        count += 1
                if count > (len(self.peers) + 1) / 2:
                    self.commit_index = n
                    break

    async def step_down(self, term):
        self.current_term = term
        self.state = "FOLLOWER"
        self.voted_for = None
        self.last_heartbeat = time.time()

    def handle_append_entries(self, term, leader_id, prev_index, prev_term, entries, leader_commit):
        if term < self.current_term:
            return False, self.current_term

        self.last_heartbeat = time.time()
        self.leader_id = leader_id

        if prev_index >= len(self.log) or (prev_index >= 0 and self.log[prev_index]['term'] != prev_term):
            return False, self.current_term

        # Conflict resolution and log update logic here
        self.log = self.log[:prev_index+1] + entries
        if leader_commit > self.commit_index:
            self.commit_index = min(leader_commit, len(self.log) - 1)

        return True, self.current_term
