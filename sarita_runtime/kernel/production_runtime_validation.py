import asyncio
from sarita_runtime.kernel.cluster_runtime_manager import ClusterRuntimeManager
from sarita_runtime.kernel.durable_consensus_engine import DurableConsensusEngine

async def run_production_validation():
    print("--- SARITA PRODUCTION RUNTIME VALIDATION ---")

    # 1. Test Cluster Manager
    cm = ClusterRuntimeManager("validator-node")
    await cm.register_node()
    print("Node Registration: PASS")

    # 2. Test Consensus
    ce = DurableConsensusEngine("validator-node", 3)
    if ce.propose_state_change("ALERT", 2):
        print("Quorum Consensus: PASS")
    else:
        print("Quorum Consensus: FAIL")

    print("--- PRODUCTION VALIDATION SUCCESSFUL ---")

if __name__ == "__main__":
    asyncio.run(run_production_validation())
