CREATE TABLE core.task_status_history (
    id UUID PRIMARY KEY DEFAULT gen_random_uuid(),
    tenant_id UUID NOT NULL,
    trace_id UUID NOT NULL,
    hash_integridad TEXT,

    task_id UUID NOT NULL,
    from_status TEXT,
    to_status TEXT NOT NULL,

    changed_at TIMESTAMP DEFAULT now()
);
