# DISTRIBUTED CONSENSUS PROTOCOL (RAFT-BASED)

## 1. LEADER ELECTION
Nodes in the Sovereign Control Plane compete for Leadership.
- **State:** FOLLOWER -> CANDIDATE -> LEADER.
- **Heartbeat:** Leaders send heartbeats to maintain authority.
- **Quorum:** Elections require N/2 + 1 votes.

## 2. STATE REPLICATION
- Any mode change (ej. `WAR_MODE`) must be replicated to the majority of nodes before being committed.
- This prevents a single corrupt node from shutting down the entire ecosystem.

## 3. IMPLEMENTATION STRATEGY
Using **etcd** or **Consul** as the underlying consensus engine, with a Python wrapper for SARITA-specific state transitions.
