CREATE TABLE core.checklist_items (
    id UUID PRIMARY KEY DEFAULT gen_random_uuid(),
    tenant_id UUID NOT NULL,
    trace_id UUID NOT NULL,
    hash_integridad TEXT,

    checklist_id UUID NOT NULL,
    question TEXT NOT NULL,
    order_index INT NOT NULL,

    created_at TIMESTAMP DEFAULT now()
);
