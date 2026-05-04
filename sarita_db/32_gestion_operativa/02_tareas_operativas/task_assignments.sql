CREATE TABLE core.task_assignments (
    id UUID PRIMARY KEY DEFAULT gen_random_uuid(),
    tenant_id UUID NOT NULL,
    trace_id UUID NOT NULL,
    hash_integridad TEXT,

    task_id UUID NOT NULL,
    user_id UUID NOT NULL, -- Responsable

    assigned_at TIMESTAMP DEFAULT now(),
    completed_at TIMESTAMP
);
