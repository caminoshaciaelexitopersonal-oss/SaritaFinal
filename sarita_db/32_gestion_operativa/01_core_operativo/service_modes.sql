CREATE TABLE core.service_modes (
    id UUID PRIMARY KEY DEFAULT gen_random_uuid(),
    tenant_id UUID NOT NULL,
    trace_id UUID NOT NULL,
    hash_integridad TEXT,

    mode_name TEXT NOT NULL, -- presencial, virtual, hibrido
    description TEXT,

    created_at TIMESTAMP DEFAULT now()
);
