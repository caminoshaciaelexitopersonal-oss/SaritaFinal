import logging

class CryptographicEquivalenceValidator:
    """
    Validates cryptographic root and final hash equivalence.
    """
    @staticmethod
    def validate(original_graph, replayed_graph):
        orig_v = original_graph.get_all_vertices()
        repl_v = replayed_graph.get_all_vertices()

        if not orig_v or not repl_v:
            return False, "Empty vertex streams"

        results = {
            "root_hash": orig_v[0].vertex_hash == repl_v[0].vertex_hash,
            "final_hash": orig_v[-1].vertex_hash == repl_v[-1].vertex_hash,
            "causal_continuity": all(orig_v[i].vertex_hash == repl_v[i].vertex_hash for i in range(len(orig_v)))
        }

        return all(results.values()), results
