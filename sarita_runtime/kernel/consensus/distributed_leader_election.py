import asyncio
import logging
import random
import time
import json
import os

class RaftNode:
    """
    Real Raft State Machine with persistent WAL and Network Transport.
    """
    def __init__(self, node_id, peers, transport, storage):
        self.node_id = node_id
        self.peers = peers # list of peer node_ids
        self.transport = transport
        self.storage = storage

        # Persistent state (Must be backed by storage)
        state = self.storage.load_checkpoint(f"raft_{node_id}")[0] or {}
        self.current_term = state.get("current_term", 0)
        self.voted_for = state.get("voted_for", None)
        self.log = state.get("log", [])

        # Volatile state
        self.commit_index = 0
        self.last_applied = 0
        self.state = "FOLLOWER"
        self.leader_id = None

        # Leader-only state
        self.next_index = {peer: len(self.log) for peer in peers}
        self.match_index = {peer: 0 for peer in peers}

        self.election_timeout = random.uniform(1.5, 3.0)
        self.last_heartbeat = time.time()

    async def run_loop(self):
        logging.info(f"Raft: Node {self.node_id} starting real state machine loop.")
        while True:
            if self.state in ["FOLLOWER", "CANDIDATE"]:
                if time.time() - self.last_heartbeat > self.election_timeout:
                    await self.start_election()
            elif self.state == "LEADER":
                await self.broadcast_heartbeats()
            await asyncio.sleep(0.1)

    async def start_election(self):
        self.state = "CANDIDATE"
        self.current_term += 1
        self.voted_for = self.node_id
        self.last_heartbeat = time.time()
        self.election_timeout = random.uniform(1.5, 3.0)

        logging.info(f"Raft: Node {self.node_id} initiating election for term {self.current_term}")
        self._persist_state()

        votes = 1 # Vote for self
        last_log_index = len(self.log) - 1
        last_log_term = self.log[last_log_index]['term'] if last_log_index >= 0 else 0

        vote_tasks = [
            self.transport.request_vote(peer, self.current_term, self.node_id, last_log_index, last_log_term)
            for peer in self.peers
        ]

        results = await asyncio.gather(*vote_tasks)
        for granted, term in results:
            if term > self.current_term:
                await self.step_down(term)
                return
            if granted:
                votes += 1

        if votes > (len(self.peers) + 1) / 2:
            await self.become_leader()

    async def become_leader(self):
        self.state = "LEADER"
        self.leader_id = self.node_id
        logging.info(f"Raft: Node {self.node_id} ELECTED LEADER for term {self.current_term}")
        for peer in self.peers:
            self.next_index[peer] = len(self.log)
            self.match_index[peer] = 0
        await self.broadcast_heartbeats()

    async def broadcast_heartbeats(self):
        for peer in self.peers:
            prev_index = self.next_index[peer] - 1
            prev_term = self.log[prev_index]['term'] if prev_index >= 0 else 0
            entries = self.log[self.next_index[peer]:]

            success, term = await self.transport.append_entries(
                peer, self.current_term, self.node_id, prev_index, prev_term, entries, self.commit_index
            )

            if term > self.current_term:
                await self.step_down(term)
                return

            if success:
                self.next_index[peer] = len(self.log)
                self.match_index[peer] = len(self.log) - 1
                await self.update_commit_index()
            else:
                self.next_index[peer] = max(0, self.next_index[peer] - 1)

    async def update_commit_index(self):
        # Implementation of Raft commit rule
        for n in range(len(self.log) - 1, self.commit_index, -1):
            if self.log[n]['term'] == self.current_term:
                count = 1
                for peer in self.peers:
                    if self.match_index[peer] >= n:
                        count += 1
                if count > (len(self.peers) + 1) / 2:
                    self.commit_index = n
                    logging.info(f"Raft: Commit Index advanced to {self.commit_index}")
                    break

    async def step_down(self, term):
        self.current_term = term
        self.state = "FOLLOWER"
        self.voted_for = None
        self.leader_id = None
        self._persist_state()
        logging.info(f"Raft: Node {self.node_id} stepping down to term {term}")

    def _persist_state(self):
        state = {
            "current_term": self.current_term,
            "voted_for": self.voted_for,
            "log": self.log
        }
        self.storage.save_checkpoint(f"raft_{self.node_id}", state, self.current_term)
