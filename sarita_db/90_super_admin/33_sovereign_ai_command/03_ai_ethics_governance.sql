-- 90_super_admin/33_sovereign_ai_command/03_ai_ethics_governance.sql
-- FASE 33 — SOVEREIGN AI COMMAND: Ethics and Emergency

CREATE TABLE IF NOT EXISTS ai_core.ai_ethics_governance (
    id UUID PRIMARY KEY DEFAULT gen_random_uuid(),
    autonomy_limit_rules JSONB,
    moral_governance_policy TEXT,
    sovereign_restriction_level INTEGER,
    violation_incident_id UUID,
    tenant_id UUID NOT NULL,
    trace_id UUID NOT NULL,
    context_id UUID NOT NULL,
    created_at TIMESTAMPTZ DEFAULT now(),
    hash_integridad TEXT
);

CREATE TABLE IF NOT EXISTS ai_core.ai_emergency_shutdown_protocols (
    id UUID PRIMARY KEY DEFAULT gen_random_uuid(),
    protocol_type TEXT CHECK (protocol_type IN ('SOFT_FREEZE', 'HARD_QUARANTINE', 'FULL_SHUTDOWN', 'MEMORY_WIPE')),
    trigger_source_agent_id UUID,
    affected_agent_clusters UUID[],
    is_active BOOLEAN DEFAULT false,
    tenant_id UUID NOT NULL,
    trace_id UUID NOT NULL,
    context_id UUID NOT NULL,
    created_at TIMESTAMPTZ DEFAULT now(),
    hash_integridad TEXT
);
