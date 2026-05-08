-- 90_super_admin/33_sovereign_ai_command/01_global_ai_command.sql
-- FASE 33 — SOVEREIGN AI COMMAND: Command and Conflict

CREATE TABLE IF NOT EXISTS ai_core.global_ai_master_command (
    id UUID PRIMARY KEY DEFAULT gen_random_uuid(),
    command_name TEXT NOT NULL,
    hierarchy_authority_level INTEGER DEFAULT 6, -- Supreme Command
    coordination_mode TEXT CHECK (coordination_mode IN ('CENTRALIZED', 'FEDERATED', 'MILITARY', 'AUTONOMOUS')),
    active_directives JSONB DEFAULT '[]',
    tenant_id UUID NOT NULL,
    trace_id UUID NOT NULL,
    context_id UUID NOT NULL,
    created_at TIMESTAMPTZ DEFAULT now(),
    hash_integridad TEXT
);

CREATE TABLE IF NOT EXISTS ai_core.ai_cognitive_arbitration (
    id UUID PRIMARY KEY DEFAULT gen_random_uuid(),
    agent_a_id UUID NOT NULL,
    agent_b_id UUID NOT NULL,
    conflict_context TEXT,
    hierarchical_winner_id UUID,
    was_isolated BOOLEAN DEFAULT false, -- If one agent was corrupt
    tenant_id UUID NOT NULL,
    trace_id UUID NOT NULL,
    context_id UUID NOT NULL,
    created_at TIMESTAMPTZ DEFAULT now(),
    hash_integridad TEXT
);
