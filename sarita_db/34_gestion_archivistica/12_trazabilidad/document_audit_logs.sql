-- Trazabilidad Forense
CREATE TABLE archival.document_audit_logs_extended (
    id UUID PRIMARY KEY DEFAULT gen_random_uuid(),
    tenant_id UUID NOT NULL,
    trace_id UUID NOT NULL,
    hash_integridad TEXT,

    document_id UUID NOT NULL,
    user_id UUID NOT NULL,

    action_type TEXT NOT NULL,
    details JSONB,

    created_at TIMESTAMP DEFAULT now()
);
