CREATE TABLE governance.departments (
    id UUID PRIMARY KEY DEFAULT gen_random_uuid(),
    tenant_id UUID NOT NULL,
    entity_id UUID NOT NULL, -- FK en 20_global
    name TEXT NOT NULL,
    parent_id UUID, -- FK en 20_global
    created_at TIMESTAMP DEFAULT now(),
    hash_integridad TEXT,
    trace_id UUID
);
