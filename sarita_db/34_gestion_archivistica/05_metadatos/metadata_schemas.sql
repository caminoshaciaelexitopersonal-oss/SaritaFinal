-- Metadatos Dinámicos
CREATE TABLE archival.metadata_schemas (
    id UUID PRIMARY KEY DEFAULT gen_random_uuid(),
    tenant_id UUID NOT NULL,
    trace_id UUID NOT NULL,
    hash_integridad TEXT,

    name TEXT NOT NULL,
    description TEXT,

    created_at TIMESTAMP DEFAULT now()
);
