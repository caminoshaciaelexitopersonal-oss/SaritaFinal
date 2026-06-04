import logging
from sarita_runtime.kernel.runtime_graph.unified_execution_graph import UnifiedExecutionGraph
from sarita_runtime.kernel.runtime_replay_engine import RuntimeReplayEngine

class NonDivergenceValidator:
    """
    Certifies that Production and Replay states are identical (Phase 78.6).
    """
    @staticmethod
    def validate(production_graph: UnifiedExecutionGraph):
        production_graph.wait_for_convergence()

        # 1. Capture Production State
        prod_vertices = production_graph.get_all_vertices()
        prod_ownership = dict(production_graph.ownership)
        prod_pressure = production_graph.global_pressure

        # 2. Perform Replay
        replay_engine = RuntimeReplayEngine(production_graph.ledger)
        replayed_graph = replay_engine.reconstruct_graph_state()
        replayed_graph.wait_for_convergence()

        # 3. Compare
        replay_vertices = replayed_graph.get_all_vertices()
        replay_ownership = replayed_graph.ownership
        replay_pressure = replayed_graph.global_pressure

        results = {
            "vertex_match": len(prod_vertices) == len(replay_vertices),
            "ownership_match": prod_ownership == replay_ownership,
            "pressure_match": abs(prod_pressure - replay_pressure) < 1e-9,
            "hash_alignment": all(v_p.vertex_hash == v_r.vertex_hash for v_p, v_r in zip(prod_vertices, replay_vertices))
        }

        is_certified = all(results.values())
        return is_certified, results
