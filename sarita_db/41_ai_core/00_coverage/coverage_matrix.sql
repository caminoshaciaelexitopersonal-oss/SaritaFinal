-- 41_ai_core/00_coverage/coverage_matrix.sql
CREATE TABLE ai.agent_coverage_matrix (
    id UUID PRIMARY KEY DEFAULT gen_random_uuid(),
    tenant_id UUID NOT NULL,
    domain TEXT NOT NULL,
    entity_table TEXT NOT NULL,
    entity_type TEXT NOT NULL,
    agent_required BOOLEAN DEFAULT TRUE,
    coverage_level INT DEFAULT 1,
    trace_id UUID, -- Opcional para la configuración, pero se incluye por consistencia
    created_at TIMESTAMPTZ DEFAULT now()
);

CREATE INDEX idx_acm_tenant ON ai.agent_coverage_matrix(tenant_id);
CREATE INDEX idx_acm_domain ON ai.agent_coverage_matrix(domain);
