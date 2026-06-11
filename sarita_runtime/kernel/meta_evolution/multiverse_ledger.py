from .meta_constitution_ledger import MetaEvolutionLedger

class MultiverseLedger(MetaEvolutionLedger):
    def record_multiverse_session(self, session_id, universe_count, results_summary):
        self.record("MULTIVERSE_SESSION", {
            "session_id": session_id,
            "universe_count": universe_count,
            "summary": results_summary
        })
