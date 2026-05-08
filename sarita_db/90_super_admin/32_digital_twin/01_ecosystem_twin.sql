-- 90_super_admin/32_digital_twin/01_ecosystem_twin.sql
-- FASE 32 — DIGITAL TWIN ECOSYSTEM: State and Simulation

CREATE TABLE IF NOT EXISTS infrastructure.ecosystem_digital_twin (
    id UUID PRIMARY KEY DEFAULT gen_random_uuid(),
    twin_timestamp TIMESTAMPTZ DEFAULT now(),
    virtual_state_snapshot JSONB, -- Full operational replica state
    is_synchronized BOOLEAN DEFAULT true,
    last_sync_id UUID,
    tenant_id UUID NOT NULL,
    trace_id UUID NOT NULL,
    context_id UUID NOT NULL,
    created_at TIMESTAMPTZ DEFAULT now(),
    hash_integridad TEXT
);

CREATE TABLE IF NOT EXISTS infrastructure.predictive_simulations (
    id UUID PRIMARY KEY DEFAULT gen_random_uuid(),
    scenario_type TEXT CHECK (scenario_type IN ('FINANCIAL_EXPANSION', 'TOURISM_PRESSURE', 'IA_SATURATION', 'MULTI_TENANT_CRISIS')),
    future_projection_data JSONB,
    estimated_collapse_probability DECIMAL(5, 4),
    recommended_mitigation_id UUID,
    tenant_id UUID NOT NULL,
    trace_id UUID NOT NULL,
    context_id UUID NOT NULL,
    created_at TIMESTAMPTZ DEFAULT now(),
    hash_integridad TEXT
);
