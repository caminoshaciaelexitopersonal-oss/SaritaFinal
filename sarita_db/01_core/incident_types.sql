-- Incidentes y Soporte
CREATE TABLE core.incident_types (
    id UUID PRIMARY KEY DEFAULT gen_random_uuid(),
    tenant_id UUID NOT NULL,
    trace_id UUID NOT NULL,
    hash_integridad TEXT,

    name TEXT NOT NULL,
    severity TEXT DEFAULT 'media', -- baja, media, alta, critica

    created_at TIMESTAMP DEFAULT now()
);
