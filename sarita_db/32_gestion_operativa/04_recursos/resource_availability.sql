CREATE TABLE core.resource_availability (
    id UUID PRIMARY KEY DEFAULT gen_random_uuid(),
    tenant_id UUID NOT NULL,
    trace_id UUID NOT NULL,
    hash_integridad TEXT,

    resource_id UUID NOT NULL,
    start_time TIMESTAMP NOT NULL,
    end_time TIMESTAMP NOT NULL,

    status TEXT DEFAULT 'disponible', -- disponible, ocupado, mantenimiento

    created_at TIMESTAMP DEFAULT now()
);
