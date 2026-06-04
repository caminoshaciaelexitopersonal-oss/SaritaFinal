import logging

class ReplayEvidenceComparator:
    """
    Compares evidence chains between original and replayed execution.
    """
    @staticmethod
    def compare_vertices(original_graph, replayed_graph):
        orig_v = original_graph.get_all_vertices()
        repl_v = replayed_graph.get_all_vertices()

        if len(orig_v) != len(repl_v):
            return False, f"Vertex count mismatch: {len(orig_v)} vs {len(repl_v)}"

        for i in range(len(orig_v)):
            if orig_v[i].vertex_hash != repl_v[i].vertex_hash:
                return False, f"Hash mismatch at index {i}"

        return True, "EVIDENCE_STREAMS_EQUIVALENT"
