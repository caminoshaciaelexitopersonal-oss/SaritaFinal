from sarita_runtime.kernel.evidence_fabric.runtime_evidence_registry import RuntimeEvidenceRegistry

class ExecutionEvidenceChain:
    def __init__(self, registry: RuntimeEvidenceRegistry):
        self.registry = registry
    def anchor_causal_chain(self, telemetry_data: dict, decision_logic: str, action_result: dict):
        chain_id = self.registry.register_physical_event("system", "CAUSAL_ANCHOR", "START", {"telemetry": telemetry_data, "decision": decision_logic})
        self.registry.register_physical_event("system", "CAUSAL_REALIZATION", "COMPLETE", {"anchor_id": chain_id, "outcome": action_result})
        return chain_id
