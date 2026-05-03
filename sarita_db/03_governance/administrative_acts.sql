CREATE TABLE governance.administrative_acts (
    id UUID PRIMARY KEY DEFAULT gen_random_uuid(),
    tenant_id UUID NOT NULL,
    entity_id UUID NOT NULL, -- FK en 20_global
    issued_by UUID, -- funcionario, FK en 20_global
    act_type TEXT, -- decreto, resolución, acuerdo
    title TEXT,
    content TEXT,
    issued_at TIMESTAMP,
    status TEXT,
    created_at TIMESTAMP DEFAULT now(),
    hash_integridad TEXT,
    trace_id UUID
);
