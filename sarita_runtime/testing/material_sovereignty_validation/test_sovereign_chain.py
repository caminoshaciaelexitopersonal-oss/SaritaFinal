import unittest
import time
from sarita_runtime.kernel.sovereign_enforcement_fabric import SovereignEnforcementFabric
from sarita_runtime.kernel.runtime_graph.unified_execution_graph import UnifiedExecutionGraph
from sarita_runtime.kernel.runtime_replay_engine import RuntimeReplayEngine
from sarita_runtime.kernel.causal_replay_validator import CausalReplayValidator

class TestMaterialSovereignty(unittest.TestCase):
    def test_full_chain_validation(self):
        graph = UnifiedExecutionGraph()
        enforcement = SovereignEnforcementFabric(graph)
        enforcement.claim_hardware_path("NVME", 10, 0)
        enforcement.execute_material_io("io_1", "READ", {"buf": 0x1000})
        graph.calculate_saturation({"cpu": 0.95})
        time.sleep(1)
        replay_engine = RuntimeReplayEngine(graph.ledger)
        replayed_graph = replay_engine.reconstruct_graph_state()
        time.sleep(1)
        valid, msg = CausalReplayValidator.validate_consistency(graph, replayed_graph)
        self.assertTrue(valid, msg)
        self.assertEqual(replayed_graph.ownership["IRQ_10"], "0")
        self.assertGreater(replayed_graph.global_pressure, 0.9)

if __name__ == "__main__":
    unittest.main()
