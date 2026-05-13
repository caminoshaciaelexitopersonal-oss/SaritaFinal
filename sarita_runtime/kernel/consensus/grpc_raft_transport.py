import asyncio
import logging
import grpc
# Note: In a real environment, we would use protoc to generate these
# from a .proto file. Here we simulate the gRPC interaction logic.

class RaftTransport:
    async def send_vote_request(self, target, term, candidate_id):
        logging.info(f"gRPC: RequestVote to {target} for term {term}")
        # Simulate gRPC call to candidate's RequestVote RPC
        return True

    async def send_append_entries(self, target, term, leader_id, entries, commit_index):
        logging.info(f"gRPC: AppendEntries to {target} (term={term}, commit={commit_index})")
        # Simulate gRPC call to AppendEntries RPC
        return True

class ReplicatedLogShipper:
    def __init__(self, transport):
        self.transport = transport

    async def ship_log(self, target, term, leader_id, entries, commit_index):
        await self.transport.send_append_entries(target, term, leader_id, entries, commit_index)

class QuorumCommitValidator:
    def __init__(self, cluster_size):
        self.cluster_size = cluster_size
        self.match_indexes = {} # node_id -> match_index

    def update_match_index(self, node_id, index):
        self.match_indexes[node_id] = index

    def get_commit_index(self):
        # Determine the highest index replicated on a majority of nodes
        sorted_indexes = sorted(self.match_indexes.values(), reverse=True)
        quorum_index = (self.cluster_size // 2)
        if len(sorted_indexes) > quorum_index:
            return sorted_indexes[quorum_index]
        return 0
