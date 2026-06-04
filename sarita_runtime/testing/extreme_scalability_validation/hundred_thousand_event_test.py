import unittest
import os
import time
import logging
import gc
from sarita_runtime.kernel.runtime_graph.unified_execution_graph import UnifiedExecutionGraph
from sarita_runtime.kernel.runtime_replay_engine import RuntimeReplayEngine

class ExtremeScalabilityTest(unittest.TestCase):
    def setUp(self):
        self.db_path = f"/tmp/extreme_scale_{int(time.time())}.db"
        self.graph = UnifiedExecutionGraph(ledger_db=self.db_path)

    def tearDown(self):
        self.graph.shutdown()
        if os.path.exists(self.db_path):
            os.remove(self.db_path)
        # Clean up WAL files
        for f in [self.db_path + "-wal", self.db_path + "-shm"]:
            if os.path.exists(f): os.remove(f)

    def test_hundred_thousand_events(self):
        count = 100000
        print(f"Ingesting {count} events...")
        start = time.time()
        for i in range(count):
            self.graph.emit_event(f"t_{i}", "LOAD_TEST", {"val": i})
            if i % 10000 == 0:
                print(f"Progress: {i}/{count}")

        self.graph.wait_for_convergence(timeout=120)
        end = time.time()
        print(f"Ingestion of {count} events took {end - start:.2f}s ({(count/(end-start)):.2f} events/s)")

        # Verify Memory
        import psutil
        process = psutil.Process(os.getpid())
        mem_mb = process.memory_info().rss / 1024 / 1024
        print(f"Memory Usage: {mem_mb:.2f} MB")

        # Verify Replay Alignment
        print("Starting replay validation...")
        replay_start = time.time()
        replay_engine = RuntimeReplayEngine(self.graph.ledger)
        replayed_graph = replay_engine.reconstruct_graph_state()
        replayed_graph.wait_for_convergence(timeout=120)
        replay_end = time.time()
        print(f"Replay of {count} events took {replay_end - replay_start:.2f}s")

        self.assertEqual(len(self.graph.get_all_vertices()), len(replayed_graph.get_all_vertices()))
        replayed_graph.shutdown()

if __name__ == "__main__":
    unittest.main()
