import asyncio
import logging
import json
import os

class RaftLogReplicator:
    def __init__(self, node_id, peers, transport):
        self.node_id = node_id
        self.peers = peers
        self.transport = transport
        self.log_path = f"sarita_runtime/kernel/consensus/wal_{node_id}.json"
        self.log = self._load_log()

    def _load_log(self):
        if os.path.exists(self.log_path):
            with open(self.log_path, 'r') as f:
                return json.load(f)
        return []

    async def replicate_entry(self, term, command):
        entry = {"term": term, "command": command, "index": len(self.log)}
        self.log.append(entry)
        self._persist_log()

        # Real propagation to followers
        replication_tasks = [
            self.transport.append_entries(peer, term, self.node_id, entry)
            for peer in self.peers
        ]
        await asyncio.gather(*replication_tasks)
        return entry['index']

    def _persist_log(self):
        with open(self.log_path, 'w') as f:
            json.dump(self.log, f)

class RaftCommitPipeline:
    def __init__(self, quorum_size):
        self.quorum_size = quorum_size
        self.match_indexes = {}

    def report_match(self, peer_id, index):
        self.match_indexes[peer_id] = index
        return self._calculate_commit_index()

    def _calculate_commit_index(self):
        # Implementation of majority commit logic
        indices = sorted(self.match_indexes.values(), reverse=True)
        if len(indices) >= self.quorum_size:
            return indices[self.quorum_size - 1]
        return 0
