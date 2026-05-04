CREATE TABLE core.automation_execution_logs (
    id UUID PRIMARY KEY DEFAULT gen_random_uuid(),
    tenant_id UUID NOT NULL,
    trace_id UUID NOT NULL,
    hash_integridad TEXT,

    rule_id UUID NOT NULL,
    target_id UUID, -- Lead ID, Convo ID, etc

    status TEXT DEFAULT 'success', -- success, failed
    execution_time_ms INT,

    created_at TIMESTAMP DEFAULT now()
);
