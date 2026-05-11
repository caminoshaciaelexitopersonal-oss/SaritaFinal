-- 40.1 — IMPLEMENTAR RLS REAL (ANTI-TENANT LEAKAGE)
-- This script activates real security isolation.

-- 1. Enable RLS on critical tables
ALTER TABLE core.tenants ENABLE ROW LEVEL SECURITY;
ALTER TABLE core.tenant_modules ENABLE ROW LEVEL SECURITY;
ALTER TABLE identity.roles ENABLE ROW LEVEL SECURITY;
ALTER TABLE finance.global_wallets ENABLE ROW LEVEL SECURITY;
ALTER TABLE finance.sovereign_ledger_global ENABLE ROW LEVEL SECURITY;
ALTER TABLE ai_core.agent_memory_episodic ENABLE ROW LEVEL SECURITY;
ALTER TABLE erp.corporate_puc ENABLE ROW LEVEL SECURITY;

-- 2. Define Base Isolation Policy
-- Using session variable 'app.current_tenant_id' for context
CREATE POLICY tenant_isolation_policy ON core.tenants
    USING (id = current_setting('app.current_tenant_id')::UUID);

CREATE POLICY wallet_isolation_policy ON finance.global_wallets
    USING (tenant_id = current_setting('app.current_tenant_id')::UUID);

CREATE POLICY ledger_isolation_policy ON finance.sovereign_ledger_global
    USING (tenant_id = current_setting('app.current_tenant_id')::UUID);

CREATE POLICY ai_memory_isolation_policy ON ai_core.agent_memory_episodic
    USING (tenant_id = current_setting('app.current_tenant_id')::UUID);

-- 3. Forensic Access Audit Table
CREATE TABLE IF NOT EXISTS infrastructure.forensic_access_audit (
    id UUID PRIMARY KEY DEFAULT gen_random_uuid(),
    attempted_tenant_id UUID,
    actual_tenant_id UUID,
    query_text TEXT,
    is_blocked BOOLEAN DEFAULT false,
    trace_id UUID NOT NULL,
    context_id UUID NOT NULL,
    created_at TIMESTAMPTZ DEFAULT now(),
    hash_integridad TEXT
);
