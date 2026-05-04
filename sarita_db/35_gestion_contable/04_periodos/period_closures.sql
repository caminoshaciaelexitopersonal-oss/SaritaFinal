CREATE TABLE accounting.period_closures (
    id UUID PRIMARY KEY DEFAULT gen_random_uuid(),
    tenant_id UUID NOT NULL,
    trace_id UUID NOT NULL,
    hash_integridad TEXT,

    period_id UUID NOT NULL,
    closed_by UUID NOT NULL,

    closure_date TIMESTAMP DEFAULT now(),
    audit_snapshot_hash TEXT, -- Hash de todo el balance al cierre

    created_at TIMESTAMP DEFAULT now()
);
