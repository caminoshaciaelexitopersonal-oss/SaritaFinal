CREATE TABLE core.automation_failures (
    id UUID PRIMARY KEY DEFAULT gen_random_uuid(),
    tenant_id UUID NOT NULL,
    trace_id UUID NOT NULL,
    hash_integridad TEXT,

    execution_id UUID NOT NULL,
    error_message TEXT NOT NULL,
    payload_at_failure JSONB,

    is_resolved BOOLEAN DEFAULT false,
    created_at TIMESTAMP DEFAULT now()
);
